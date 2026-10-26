"""Rebuild reviewed views in memory and reconcile against exported results.
Run with Python 3.10+ from any directory; standard library only. No network calls.
"""
from pathlib import Path
import csv,hashlib,json,sqlite3

ROOT=Path(__file__).resolve().parents[1]
def main():
    db=ROOT/'data/analysis.sqlite';before=hashlib.sha256(db.read_bytes()).hexdigest()
    with sqlite3.connect(db.as_uri()+'?mode=ro',uri=True) as source:
        con=sqlite3.connect(':memory:');source.backup(con)
    con.row_factory=sqlite3.Row
    for prefix in ['Q20','Q21','Q22']:
        con.executescript(next((ROOT/'sql').glob(prefix+'*.sql')).read_text(encoding='utf-8'))
    totals=tuple(con.execute('select count(*),count(distinct tx_hash),count(distinct tx_from) from events').fetchone())
    assert totals==(15123,14300,2086)
    actual=[dict(r) for r in con.execute("select * from weekly_trend where week_utc>='2026-08-24' order by week_utc")]
    with (ROOT/'data/每周趋势_8周.csv').open(encoding='utf-8-sig',newline='') as f:expected=list(csv.DictReader(f))
    assert len(actual)==len(expected)==8
    for a,b in zip(actual,expected):
        for key in ['week_utc','active_addresses','transactions','event_rows']:assert str(a[key])==b[key],key
        assert abs(a['usd_estimate']-float(b['usd_estimate']))<=1e-6
    retention=[dict(r) for r in con.execute("select * from cohort_retention where cohort_week>='2026-08-24'")]
    common={r['cohort_week'] for r in retention if r['week_offset']==2 and r['mature']}
    n=sum(r['cohort_size'] for r in retention if r['week_offset']==2 and r['cohort_week'] in common)
    counts=[sum(r['returning_addresses'] for r in retention if r['week_offset']==k and r['cohort_week'] in common) for k in [1,2]]
    assert n==806 and counts==[154,149]
    ranked=list(con.execute(next((ROOT/'sql').glob('Q30*.sql')).read_text(encoding='utf-8')))
    latest=[r for r in ranked if r['week_utc']=='2026-10-12'];head=[r for r in latest if r['usd_rank']<=r['top1_count']]
    share=sum(r['usd_estimate'] for r in head)/sum(r['usd_estimate'] for r in latest)
    assert len(head)==6 and round(share*100,2)==18.61
    assert hashlib.sha256(db.read_bytes()).hexdigest()==before
    con.close()
    print(json.dumps({'passed':True,'network_calls':0,'original_database_unchanged':True,'event_transaction_origin_counts':totals,'weekly_rows_checked':8,'same_mature_cohorts_N':n,'W1_W2_counts':counts,'latest_amount_head_n':len(head),'latest_amount_head_share':share},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
