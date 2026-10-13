# Ingest report

Written by `uv run p2 ingest`.
It lists every document in this corpus that ingest added, with what the cleaning pass did and anything that looks wrong.
Running ingest again adds to the table and replaces the "last run" section, and `uv run p2 ingest --report` rewrites it for the documents in docs/ now, after you removed some.

## Summary

- Documents: 220 (the final check needs at least 200)
- Words: 400,276
- Estimated tokens (words times 1.4): 560,386 (`p2 check` warns above 800,000 and fails above 1,000,000)
- Flagged documents: 0

## Documents

| docid | words | characters per page | flags | cleaning |
|---|---:|---:|---|---|
| `ml030140543` | 2,045 | 1938 | - | 2 running line(s) removed |
| `ml030160004` | 1,362 | 1859 | - | 2 running line(s) removed |
| `ml030240029` | 1,239 | 2093 | - | - |
| `ml030350473` | 4,657 | 1517 | - | 2 running line(s) removed |
| `ml031550258` | 2,597 | 2474 | - | 2 running line(s) removed |
| `ml031700033` | 1,786 | 2525 | - | 2 running line(s) removed |
| `ml031750146` | 1,249 | 1749 | - | 2 running line(s) removed |
| `ml031750847` | 1,341 | 2338 | - | - |
| `ml031830015` | 2,414 | 2333 | - | 2 running line(s) removed |
| `ml032160016` | 1,699 | 2450 | - | - |
| `ml032250135` | 2,165 | 2919 | - | 2 running line(s) removed |
| `ml032320470` | 1,994 | 2218 | - | 2 running line(s) removed |
| `ml032410215` | 1,989 | 2285 | - | 2 running line(s) removed |
| `ml032410430` | 1,581 | 2156 | - | 2 running line(s) removed |
| `ml032480905` | 2,042 | 2334 | - | 2 running line(s) removed |
| `ml032520011` | 2,244 | 2551 | - | 2 running line(s) removed |
| `ml032520821` | 1,491 | 2067 | - | - |
| `ml032681003` | 1,138 | 1590 | - | 2 running line(s) removed |
| `ml032760027` | 1,354 | 1871 | - | 2 running line(s) removed |
| `ml032960205` | 1,265 | 1823 | - | 2 running line(s) removed |
| `ml033250492` | 1,593 | 1890 | - | 2 running line(s) removed |
| `ml033390164` | 1,471 | 1804 | - | 2 running line(s) removed |
| `ml040050433` | 1,954 | 2205 | - | 2 running line(s) removed |
| `ml040140460` | 1,849 | 1810 | - | 2 running line(s) removed |
| `ml040330279` | 1,944 | 1971 | - | 2 running line(s) removed |
| `ml040500336` | 1,963 | 1974 | - | 2 running line(s) removed |
| `ml040540778` | 1,937 | 2671 | - | 2 running line(s) removed |
| `ml040580454` | 1,679 | 1966 | - | 2 running line(s) removed |
| `ml040711214` | 1,893 | 2558 | - | 2 running line(s) removed |
| `ml040770145` | 1,625 | 2232 | - | 2 running line(s) removed |
| `ml041130396` | 2,214 | 2143 | - | 2 running line(s) removed |
| `ml041170030` | 2,264 | 2213 | - | 2 running line(s) removed |
| `ml041170480` | 2,403 | 2680 | - | 2 running line(s) removed |
| `ml041460357` | 2,191 | 2477 | - | 2 running line(s) removed |
| `ml041760122` | 1,607 | 1926 | - | 1 running line(s) removed |
| `ml041810535` | 3,420 | 2323 | - | 3 running line(s) removed |
| `ml041950006` | 2,047 | 2240 | - | 2 running line(s) removed |
| `ml042180094` | 1,905 | 2178 | - | 2 running line(s) removed |
| `ml042510509` | 2,242 | 2621 | - | 2 running line(s) removed |
| `ml042730010` | 2,291 | 2579 | - | 2 running line(s) removed |
| `ml042950687` | 2,117 | 2105 | - | 2 running line(s) removed |
| `ml043280614` | 1,247 | 1790 | - | 2 running line(s) removed |
| `ml043510005` | 1,837 | 1788 | - | 2 running line(s) removed |
| `ml050100104` | 1,025 | 1700 | - | 2 running line(s) removed |
| `ml050350091` | 996 | 1718 | - | 1 running line(s) removed |
| `ml050400090` | 1,248 | 2189 | - | 2 running line(s) removed |
| `ml050490364` | 1,372 | 1820 | - | 2 running line(s) removed |
| `ml050530400` | 2,032 | 1930 | - | 2 running line(s) removed |
| `ml050590234` | 1,252 | 1715 | - | 2 running line(s) removed |
| `ml050680335` | 2,687 | 2904 | - | 2 running line(s) removed |
| `ml050730093` | 1,460 | 1973 | - | 2 running line(s) removed |
| `ml050870005` | 1,560 | 2087 | - | 2 running line(s) removed |
| `ml050870351` | 1,248 | 1741 | - | 2 running line(s) removed |
| `ml050890089` | 2,077 | 1642 | - | 3 running line(s) removed |
| `ml050960474` | 1,305 | 2209 | - | 2 running line(s) removed |
| `ml051080466` | 1,230 | 1457 | - | 2 running line(s) removed |
| `ml051080499` | 1,861 | 1792 | - | 2 running line(s) removed; reference list dropped, 733 characters (heading) |
| `ml051180228` | 1,158 | 1386 | - | 2 running line(s) removed |
| `ml051530520` | 1,661 | 1903 | - | 2 running line(s) removed |
| `ml051640539` | 5,907 | 1275 | - | 2 running line(s) removed |
| `ml051740051` | 1,605 | 2730 | - | 2 running line(s) removed |
| `ml051740299` | 1,453 | 1918 | - | 2 running line(s) removed |
| `ml051780073` | 1,283 | 2232 | - | 2 running line(s) removed |
| `ml051780232` | 2,304 | 2186 | - | 2 running line(s) removed |
| `ml051890406` | 1,231 | 1719 | - | 2 running line(s) removed |
| `ml051920213` | 917 | 1580 | - | 2 running line(s) removed |
| `ml052020249` | 1,532 | 1802 | - | 2 running line(s) removed |
| `ml052150404` | 1,101 | 1877 | - | 2 running line(s) removed |
| `ml052280011` | 1,983 | 2158 | - | 2 running line(s) removed |
| `ml052570220` | 1,356 | 2299 | - | 2 running line(s) removed |
| `ml052720579` | 1,661 | 1653 | - | 3 running line(s) removed |
| `ml052910008` | 1,724 | 2320 | - | 2 running line(s) removed |
| `ml053060039` | 1,762 | 1754 | - | 2 running line(s) removed |
| `ml053060311` | 2,017 | 1966 | - | 2 running line(s) removed |
| `ml053110349` | 906 | 2068 | - | - |
| `ml053200005` | 1,193 | 2631 | - | - |
| `ml053200013` | 810 | 1922 | - | - |
| `ml053340032` | 931 | 1642 | - | 2 running line(s) removed |
| `ml053470469` | 978 | 1732 | - | 2 running line(s) removed |
| `ml060100450` | 1,058 | 1894 | - | 2 running line(s) removed |
| `ml060110024` | 1,574 | 1769 | - | 2 running line(s) removed |
| `ml060170102` | 1,656 | 2313 | - | 2 running line(s) removed |
| `ml060330540` | 1,016 | 1655 | - | 2 running line(s) removed |
| `ml060540038` | 3,704 | 2890 | - | 2 running line(s) removed |
| `ml060580510` | 1,178 | 1365 | - | 2 running line(s) removed |
| `ml060880311` | 1,218 | 1664 | - | 2 running line(s) removed |
| `ml061360026` | 3,592 | 2579 | - | 3 running line(s) removed |
| `ml061510292` | 1,980 | 2205 | - | 2 running line(s) removed |
| `ml061720214` | 1,371 | 2370 | - | 1 running line(s) removed |
| `ml061790443` | 1,396 | 2454 | - | 2 running line(s) removed |
| `ml061870545` | 1,203 | 2810 | - | - |
| `ml062010365` | 5,597 | 1269 | - | 3 running line(s) removed |
| `ml062060013` | 2,872 | 2141 | - | 3 running line(s) removed |
| `ml062070124` | 1,884 | 2179 | - | 2 running line(s) removed |
| `ml062220339` | 893 | 2075 | - | - |
| `ml062330295` | 1,092 | 2511 | - | - |
| `ml062440467` | 870 | 1535 | - | 2 running line(s) removed |
| `ml062490133` | 1,661 | 2380 | - | 2 running line(s) removed |
| `ml062490396` | 1,423 | 2492 | - | 2 running line(s) removed |
| `ml062570468` | 1,433 | 1903 | - | 2 running line(s) removed |
| `ml062710079` | 1,834 | 2089 | - | 2 running line(s) removed |
| `ml062790341` | 1,548 | 2661 | - | 2 running line(s) removed |
| `ml062840608` | 1,902 | 2122 | - | 2 running line(s) removed |
| `ml062890437` | 1,654 | 2156 | - | 2 running line(s) removed |
| `ml062910111` | 1,333 | 1794 | - | 2 running line(s) removed |
| `ml063000104` | 1,080 | 1881 | - | 2 running line(s) removed |
| `ml063110327` | 2,067 | 2381 | - | 2 running line(s) removed |
| `ml063380232` | 1,824 | 2514 | - | 2 running line(s) removed |
| `ml063470020` | 1,872 | 2186 | - | 3 running line(s) removed |
| `ml063540138` | 1,410 | 1832 | - | 2 running line(s) removed |
| `ml070100459` | 1,068 | 1780 | - | - |
| `ml070120205` | 742 | 1748 | - | - |
| `ml070190328` | 1,863 | 1830 | - | 3 running line(s) removed |
| `ml070390066` | 802 | 1405 | - | 2 running line(s) removed |
| `ml070440238` | 1,457 | 2015 | - | 2 running line(s) removed |
| `ml070510034` | 662 | 1506 | - | - |
| `ml070610424` | 1,099 | 1858 | - | 2 running line(s) removed |
| `ml070710036` | 1,947 | 2618 | - | 2 running line(s) removed |
| `ml070710233` | 4,175 | 2832 | - | 2 running line(s) removed |
| `ml070811111` | 2,039 | 2041 | - | 2 running line(s) removed |
| `ml071010303` | 1,741 | 2946 | - | 1 running line(s) removed |
| `ml071090170` | 1,261 | 2162 | - | 2 running line(s) removed |
| `ml071100075` | 1,256 | 1716 | - | 2 running line(s) removed |
| `ml071150051` | 1,035 | 1410 | - | 2 running line(s) removed |
| `ml071220351` | 2,473 | 2736 | - | 2 running line(s) removed |
| `ml071410230` | 1,950 | 1979 | - | 2 running line(s) removed |
| `ml071510558` | 1,934 | 1928 | - | 2 running line(s) removed |
| `ml071590308` | 3,526 | 1223 | - | 3 running line(s) removed |
| `ml071650373` | 1,614 | 1686 | - | 3 running line(s) removed |
| `ml071760544` | 1,514 | 2069 | - | 2 running line(s) removed |
| `ml071900368` | 1,625 | 2607 | - | 2 running line(s) removed |
| `ml071920090` | 2,685 | 2570 | - | 2 running line(s) removed |
| `ml071920514` | 1,811 | 2470 | - | 2 running line(s) removed |
| `ml072150614` | 1,314 | 1867 | - | 2 running line(s) removed |
| `ml072270127` | 2,743 | 3174 | - | 2 running line(s) removed |
| `ml072390061` | 1,721 | 1968 | - | 2 running line(s) removed |
| `ml072500291` | 2,086 | 1849 | - | 4 running line(s) removed |
| `ml072530077` | 2,417 | 1693 | - | 4 running line(s) removed |
| `ml072700212` | 1,811 | 1832 | - | 3 running line(s) removed |
| `ml072760661` | 2,240 | 2203 | - | 3 running line(s) removed |
| `ml072780394` | 1,451 | 2456 | - | 2 running line(s) removed |
| `ml072910750` | 1,502 | 1997 | - | 2 running line(s) removed |
| `ml073450262` | 2,898 | 2603 | - | 2 running line(s) removed |
| `ml073540243` | 991 | 1686 | - | 2 running line(s) removed |
| `ml080040353` | 2,049 | 1929 | - | 2 running line(s) removed |
| `ml080370453` | 1,909 | 2285 | - | 2 running line(s) removed |
| `ml080440014` | 2,553 | 2774 | - | 2 running line(s) removed |
| `ml080650492` | 1,209 | 1756 | - | 2 running line(s) removed |
| `ml080710054` | 1,898 | 2191 | - | 2 running line(s) removed |
| `ml080780091` | 1,833 | 1817 | - | 2 running line(s) removed |
| `ml080880115` | 2,051 | 2715 | - | 2 running line(s) removed |
| `ml081120649` | 1,517 | 2019 | - | 2 running line(s) removed |
| `ml081130668` | 1,446 | 2029 | - | 2 running line(s) removed |
| `ml081790193` | 6,361 | 1194 | - | 2 running line(s) removed |
| `ml081830163` | 1,167 | 1933 | - | 2 running line(s) removed |
| `ml081850581` | 2,219 | 3147 | - | 2 running line(s) removed |
| `ml081890131` | 1,086 | 1892 | - | 2 running line(s) removed |
| `ml081900401` | 994 | 1443 | - | 2 running line(s) removed |
| `ml082460249` | 1,532 | 2017 | - | 2 running line(s) removed |
| `ml082480153` | 1,412 | 2583 | - | 2 running line(s) removed |
| `ml082540130` | 2,000 | 2580 | - | 2 running line(s) removed |
| `ml082730593` | 1,632 | 2315 | - | 2 running line(s) removed |
| `ml082840609` | 1,790 | 2426 | - | 2 running line(s) removed |
| `ml083080368` | 1,041 | 1758 | - | 2 running line(s) removed |
| `ml083250226` | 1,135 | 2079 | - | 2 running line(s) removed |
| `ml083450280` | 1,855 | 2094 | - | 2 running line(s) removed |
| `ml090290185` | 1,407 | 2473 | - | 2 running line(s) removed |
| `ml090300546` | 1,475 | 2417 | - | 1 running line(s) removed |
| `ml090340754` | 898 | 1600 | - | 2 running line(s) removed |
| `ml090370785` | 2,757 | 2430 | - | 2 running line(s) removed |
| `ml090500018` | 2,386 | 2378 | - | 2 running line(s) removed |
| `ml090540218` | 1,148 | 2010 | - | 1 running line(s) removed |
| `ml090830184` | 1,222 | 1729 | - | 2 running line(s) removed |
| `ml090920401` | 2,341 | 2146 | - | 2 running line(s) removed |
| `ml091050027` | 1,234 | 2078 | - | 2 running line(s) removed |
| `ml091190196` | 3,925 | 2673 | - | 3 running line(s) removed |
| `ml091240039` | 1,364 | 1912 | - | 2 running line(s) removed |
| `ml091520532` | 2,038 | 2271 | - | 2 running line(s) removed |
| `ml091550527` | 1,445 | 2041 | - | 2 running line(s) removed |
| `ml091670177` | 1,731 | 2488 | - | 2 running line(s) removed |
| `ml091880072` | 1,395 | 2332 | - | 2 running line(s) removed |
| `ml091890514` | 1,459 | 2081 | - | 2 running line(s) removed |
| `ml091940257` | 2,080 | 2371 | - | 2 running line(s) removed |
| `ml091940489` | 1,099 | 2484 | - | - |
| `ml091980474` | 1,257 | 1737 | - | 2 running line(s) removed |
| `ml092120085` | 1,391 | 1969 | - | 2 running line(s) removed |
| `ml092190302` | 2,012 | 2268 | - | 2 running line(s) removed |
| `ml092230554` | 1,366 | 2346 | - | 2 running line(s) removed |
| `ml092250360` | 3,311 | 2300 | - | 2 running line(s) removed |
| `ml092390194` | 2,281 | 2926 | - | 2 running line(s) removed |
| `ml092440545` | 2,143 | 2844 | - | 2 running line(s) removed |
| `ml092510055` | 1,061 | 1841 | - | 2 running line(s) removed |
| `ml092520457` | 1,421 | 2518 | - | 2 running line(s) removed |
| `ml092650761` | 8,019 | 1482 | - | 2 running line(s) removed |
| `ml092680467` | 821 | 1417 | - | 2 running line(s) removed |
| `ml092930025` | 2,075 | 2769 | - | 2 running line(s) removed |
| `ml093340392` | 1,377 | 1939 | - | 2 running line(s) removed |
| `ml093620098` | 1,103 | 1964 | - | 2 running line(s) removed |
| `ml093620107` | 1,960 | 1792 | - | 3 running line(s) removed |
| `ml093640691` | 2,268 | 2965 | - | 2 running line(s) removed |
| `ml100070106` | 1,528 | 1668 | - | 2 running line(s) removed |
| `ml100080281` | 1,495 | 2078 | - | 2 running line(s) removed |
| `ml100540070` | 1,873 | 1490 | - | 3 running line(s) removed |
| `ml100640449` | 2,455 | 2841 | - | 2 running line(s) removed |
| `ml100640465` | 1,646 | 2207 | - | 2 running line(s) removed |
| `ml101020184` | 964 | 1715 | - | 2 running line(s) removed |
| `ml101120816` | 1,530 | 2135 | - | 2 running line(s) removed |
| `ml101330321` | 1,331 | 2301 | - | 2 running line(s) removed |
| `ml101600151` | 1,148 | 2026 | - | 2 running line(s) removed |
| `ml101670005` | 2,219 | 2477 | - | 2 running line(s) removed |
| `ml101970221` | 1,728 | 1987 | - | 2 running line(s) removed |
| `ml102160735` | 961 | 1692 | - | 2 running line(s) removed |
| `ml102200071` | 1,088 | 2575 | - | - |
| `ml102210244` | 2,413 | 3060 | - | 2 running line(s) removed |
| `ml102420002` | 951 | 2219 | - | - |
| `ml102450114` | 1,692 | 2324 | - | 2 running line(s) removed |
| `ml102530012` | 1,479 | 1745 | - | 2 running line(s) removed |
| `ml102800027` | 1,758 | 1746 | - | 3 running line(s) removed |
| `ml102800456` | 4,126 | 2614 | - | 2 running line(s) removed |
| `ml121730336` | 1,742 | 2471 | - | 2 running line(s) removed |

## Not added in the last run

Nothing was left out.

## What to check by eye

Ingest cleans text by rules, and rules miss things.
Take five minutes to open the shortest, a middle one and the longest document next to its original and read one page of each.

- Search the documents for `þ`, `¼`, `(cid:` and the replacement character.
  A hit usually means the PDF's font map is wrong, which no tool can repair, so treat it as a defect and leave that document out.
- Look at the end of a few papers.
  Ingest drops a trailing reference list when it finds a References heading or a run of numbered entries.
  A paper whose list has neither can keep it, and then every author and journal name matches queries it should not.
- Open the first lines of a few documents.
  Author lists, copyright pages and tables of contents are not removed automatically, and you may want to cut them.
- Compare one table with the PDF.
  A PDF prints footnote marks as small raised digits, and the converter glues them onto the word or number next to them: `ALUMINUM1` is the heading ALUMINUM with footnote 1, and `11210,000` can be 210,000 with footnote 11.
  Quotes still match the stored text, but a number read from it can be wrong, so check before you trust a figure in a query, a judgment or an answer.
- Fix the `license` column in the manifest for every document, then run `uv run p2 license`.
  It is `unknown` until you do, and `unknown` does not pass.

## If a document is flagged as scanned

A scan is a picture of a page, so there is no text for ingest to read.
This template does not install an OCR tool, because it is large and most students never need it.
If you do need one, the opt-in route is pymupdf4llm with rapidocr, run on its own outside the template's environment:

```
uv run --no-project --with pymupdf4llm --with rapidocr python -c "import pymupdf4llm, sys, pathlib; pathlib.Path(sys.argv[2]).write_text(pymupdf4llm.to_markdown(sys.argv[1], use_ocr=True, force_ocr=True), encoding='utf-8')" scan.pdf scan.md
```

Put the resulting `.md` file in your folder and ingest the folder again.
It costs about 2 seconds a page, and OCR text needs a second look: it misreads ligatures, hyphens and numbers.
pymupdf4llm is AGPL-3.0 software, so use it only as a tool on your own machine, and do not add it to this repo's dependencies or copy its code into the repo.
