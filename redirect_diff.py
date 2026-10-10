#!/usr/bin/env python3
"""redirect-diff: compare old vs new sitemap (URL or file) and list old paths with no new equivalent. stdlib only."""
import sys, re, urllib.request, urllib.parse
def load(s):
    d=urllib.request.urlopen(urllib.request.Request(s,headers={"User-Agent":"redirect-diff/1.0"}),timeout=30).read().decode() if s.startswith("http") else open(s).read()
    locs=re.findall(r"<loc>\s*([^<]+?)\s*</loc>",d) or [l.strip() for l in d.splitlines() if l.strip()]
    return {urllib.parse.urlparse(u).path.rstrip("/") or "/" for u in locs}
def main():
    old,new=load(sys.argv[1]),load(sys.argv[2]); gone=sorted(old-new)
    print(f"old={len(old)} new={len(new)} unmatched old paths={len(gone)}")
    for p in gone[:200]: print("  ", p)
    if gone: print("\nThese need 301s or they 404 after launch. Host-ready redirect map (free check first): https://routepatch.adjudi.com/?utm_source=github&utm_medium=cli&utm_campaign=routepatch-intent-w2&utm_content=redirect-diff")
    sys.exit(1 if gone and "--fail" in sys.argv else 0)
if __name__=="__main__": main()
