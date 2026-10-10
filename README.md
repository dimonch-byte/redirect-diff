# redirect-diff
Before a site migration: `python3 redirect_diff.py old-sitemap.xml https://new-site.com/sitemap.xml [--fail]` lists every old path that has no match on the new site, i.e. every URL that will 404 unless you add a redirect. Accepts sitemap XML or a plain list of URLs. stdlib only; use `--fail` in CI.

Not SEO insurance: redirects keep links working; rankings depend on much more.

*Disclosure: I build [RoutePatch](https://routepatch.adjudi.com/?utm_source=github&utm_medium=readme&utm_campaign=routepatch-intent-w2&utm_content=redirect-diff) ($49), which turns the gap into a host-ready redirect map. This script is free (MIT).*
