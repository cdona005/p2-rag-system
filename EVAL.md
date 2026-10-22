# Evaluation report

This is the report on what you built and what the numbers let you claim.
Two kinds of text live here.

The tables between a `p2:begin` comment line and its matching `p2:end` comment line are written by `uv run p2 score` from your committed run files and answers files.
Please do not edit anything between those two lines, because `uv run p2 check` recomputes them and fails when they differ.
A table that says no runs or answers exist yet is waiting for data; run `uv run p2 score` after you commit the files it needs.

Everything else is yours.
Each prompt ends with a marker line that you replace with your own writing; `uv run p2 check --final` fails while one is left.
Write what you measured, including what did not work.
What I read for is whether each claim matches its interval, not whether the result is good news.

Words used below: recall@10, MRR@10 and nDCG@10 are the three scores, each averaged over the queries of a set; step 7 of stage 1 in the README defines them, and lecture 14 goes deeper.
A paired interval is the 95% interval of the mean difference between two systems on the same queries, found by resampling the queries 10,000 times.
When an interval includes zero, the gold set cannot tell the two systems apart, and the right words are "not distinguishable on this gold set".
The minimum detectable difference is the smallest gap this many queries could reliably show, so a difference below it is invisible to this gold set, not absent.

---

## 1. Stage 1 - the shared corpus (30 CFR Chapter I)

### What you built

For each of `dense`, `hybrid` and `rerank`, one or two sentences: the embedding model, how documents were chunked, what was fused and how, how many candidates the reranker saw, and anything you changed from the 12 and 13 lab code.

Dense:
I used BAAI/bge-small-en-v1.5 that runs through fastembed. I am using 300 word chunk with a 50 word overlap. The dense system is scored by using cosine similarity of the best chunk, and I am not using a query prefix because in testing it did not give a detectable difference of the search. 

Hybrid: 
The hybrid system is the bm25 and dense systems fused. 
Each search ranks every document, and a document earns points for its rank in each list and earns more points for a higher rank (1/(60 + rank)). The 60 comes from the lab.

Rerank:
Rerank takes the hybrid system's top 20 documents and asks claude to rerank them into a better order. It makes one claude call per query and is shown the part of the document that best matches the query and returns the order from best to worst.

I changed nothing from the labs other than using chunks of 300 words rather than whole articles.

---

### Practice queries (20)

Scores per system.

<!-- p2:begin shared-practice -->
| System | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| bm25 | 0.625 | 0.507 | 0.518 |
| dense | 0.558 | 0.562 | 0.480 |
| hybrid | 0.592 | 0.471 | 0.444 |
| rerank | 0.758 | 0.800 | 0.769 |

20 judged queries; nDCG uses binary labels; a random ranking of the 2,484 documents would get recall@10 near 0.004.
<!-- p2:end shared-practice -->

The same scores per query class.

<!-- p2:begin shared-practice-classes -->
| System | Metric | identifier (n=7) | paraphrase (n=7) | mixed (n=6) |
| --- | --- | ---: | ---: | ---: |
| bm25 | Recall@10 | 1.000 | 0.000 | 0.917 |
| bm25 | MRR@10 | 0.810 | 0.000 | 0.746 |
| bm25 | nDCG@10 | 0.857 | 0.000 | 0.728 |
| dense | Recall@10 | 0.214 | 0.595 | 0.917 |
| dense | MRR@10 | 0.333 | 0.714 | 0.653 |
| dense | nDCG@10 | 0.211 | 0.593 | 0.661 |
| hybrid | Recall@10 | 0.500 | 0.405 | 0.917 |
| hybrid | MRR@10 | 0.514 | 0.154 | 0.792 |
| hybrid | nDCG@10 | 0.397 | 0.203 | 0.779 |
| rerank | Recall@10 | 0.714 | 0.595 | 1.000 |
| rerank | MRR@10 | 0.714 | 0.714 | 1.000 |
| rerank | nDCG@10 | 0.714 | 0.626 | 1.000 |
<!-- p2:end shared-practice-classes -->

Differences between every pair of systems, each with its paired interval and the minimum detectable difference.

<!-- p2:begin shared-practice-pairs -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| dense minus bm25 | Recall@10 | -0.067 | [-0.350, +0.225] | 0.415 | not distinguishable |
| dense minus bm25 | MRR@10 | +0.055 | [-0.225, +0.343] | 0.412 | not distinguishable |
| dense minus bm25 | nDCG@10 | -0.039 | [-0.302, +0.231] | 0.385 | not distinguishable |
| hybrid minus bm25 | Recall@10 | -0.033 | [-0.250, +0.192] | 0.324 | not distinguishable |
| hybrid minus bm25 | MRR@10 | -0.036 | [-0.178, +0.084] | 0.193 | not distinguishable |
| hybrid minus bm25 | nDCG@10 | -0.075 | [-0.238, +0.075] | 0.228 | not distinguishable |
| hybrid minus dense | Recall@10 | +0.033 | [-0.125, +0.192] | 0.231 | not distinguishable |
| hybrid minus dense | MRR@10 | -0.091 | [-0.305, +0.110] | 0.300 | not distinguishable |
| hybrid minus dense | nDCG@10 | -0.036 | [-0.199, +0.113] | 0.227 | not distinguishable |
| rerank minus bm25 | Recall@10 | +0.133 | [-0.100, +0.358] | 0.340 | not distinguishable |
| rerank minus bm25 | MRR@10 | +0.293 | [+0.043, +0.533] | 0.353 | rerank higher |
| rerank minus bm25 | nDCG@10 | +0.251 | [+0.022, +0.466] | 0.323 | rerank higher |
| rerank minus dense | Recall@10 | +0.200 | [+0.050, +0.367] | 0.224 | rerank higher |
| rerank minus dense | MRR@10 | +0.237 | [+0.083, +0.408] | 0.239 | rerank higher |
| rerank minus dense | nDCG@10 | +0.289 | [+0.149, +0.443] | 0.214 | rerank higher |
| rerank minus hybrid | Recall@10 | +0.167 | [+0.058, +0.292] | 0.166 | rerank higher |
| rerank minus hybrid | MRR@10 | +0.329 | [+0.164, +0.504] | 0.246 | rerank higher |
| rerank minus hybrid | nDCG@10 | +0.325 | [+0.199, +0.453] | 0.184 | rerank higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time.
<!-- p2:end shared-practice-pairs -->

The 40 test queries have no answer key in this repo.
Your test run files are scored by the course and the score comes back to you as feedback, so nothing goes here for them.

### What the intervals let you claim

Which differences are distinguishable from zero and which are not?
What is the minimum detectable difference at 20 queries, and what does that say about any gap smaller than it?
Which claim from lecture 12 or 13 did your numbers support, and which did they leave open?

The practice queries would let me claim that rerank is better than hybrid by +0.33MRR@10, which matches the interval of [+0.164, +0.504]. However, this only works when the relevant document is already in the top 20.
All of the dense, hybrid, and bm25 pairs are indistinguishable.
The minimum detectable difference is between 0.17 and 0.42, depending on the pair and metric. A smaller gap cannot be distinguished from noise, so the 20 queries cannot reliably confirm a gap that small. 

From the lectures, fusion helps when one retriever fails and its partner catches it, but it does not know which one is correct. This can pull the score down, and in my data, bm25 was very weak on paraphrase questions and strong on identifier questions. My systems fit the lecture's claim but cannot be verified with the data.

---

## 2. Stage 1 - cited answers on the 12 shared questions

<!-- p2:begin answers -->
| Label | System | Verified (in) | 95% interval | not_found (in) | Declined (out) | 95% interval | Quotes found |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| rerank | rerank | 8 of 8 (100%) | [0.676, 1.000] | 0 of 8 (0%) | 4 of 4 (100%) | [0.510, 1.000] | 13 of 13 |
<!-- p2:end answers -->

Which system answered, and why that one?
What did you change in `prompts/answer.txt`, if anything, and did the verified share or the declined share move?

Then read three in-corpus answers that `uv run p2 verify` passed.
For each one, open the cited chunk and say whether the quote really supports the claim next to it.
The check proves a quote is a real piece of the chunk and cannot prove that it supports the claim, so this reading is the part only you can do.

I used rerank to answer because it had the best results on my practice queries. 
I did not change anything in prompts/answers.txt. 

The first one I verified was "Within how many minutes must a mine operator call MSHA after an accident that kills a miner?", and the first document that rerank returned had the answer of 15 minutes.
The second answer I checked is: "How high must berms or guardrails be on the banks of roadways at metal and nonmetal mines?", which is answered in the first few lines of the top document returned.
The third answer I verified was: "At what depth does OSHA require a construction trench to have a protective system such as shoring or a trench box?", which is one of the questions the corpus cannot answer. The first result was relevant to the question.


---

## 3. Stage 2 - your corpus and your gold set

### The corpus

What is it, where did it come from, how many documents and how many megabytes, and what is the license basis for publishing it?
Name the one or two documents you were least sure about and what you decided.
Say which of the allowed sources in the brief it comes from.

My corpus is the Nuclear Regulatory Commission Information Notices from 2003-2010. There are 220 documents at 2.8 MB. These documents are written by a federal agency, so they are US government documents.
This source is allowed per the brief because it is US federal government works, and the manifest license is us-gov-public-domain, the source is nrc.gov, and p2 license found 0 problems offline and online had nothing to compare.

There was one document that was flagged for needing third-party credit to use the figures (ml041260136). I decided to delete the document from the corpus, even though the document did not actually have the figures in it. 

### The gold set

How many queries, how many with origin `hand` and how many with origin `claude`, and which query classes did you use and why?
How did you decide that a document is relevant: write your relevance rule in two or three sentences, the way the brief does for the shared corpus.
How did you find candidates (the systems' top 10, a keyword search, reading), and did you read every document before you labeled it?
Your labels are binary (`rel` 1) unless you say otherwise: if you use graded labels, declare the scale here, for example 2 means the document answers the query fully and 1 means it helps.

My gold set has 60 queries, 20 hand and 40 from claude. I used the classes identifier, paraphrase, mixed, and typo. Identifier is useful for finding exact information notices, paraphrase tests how many users would search, mixed tests whether the RAG system can find documents with identifiers and paraphrasing, and typo covers the cases where users misspell a word.

I read all of the notices i put in qrels.txt, and made queries by reading notices randomly and making a query that fits the notice.. I searched the others with grep and reading the matching passage before labeling.

A notice is relevant when it contains the information the query asks about, such as incident, plant name, or action.
If the query does not name a plant, a notice on the same incident counts and so do supplements or revisions.
A notice that mentions the topic or cites a different notice does not count.


---

## 4. Stage 2 - results on your corpus

Scores per system on your gold set.

<!-- p2:begin own -->
| System | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| bm25 | 0.983 | 0.921 | 0.933 |
| dense | 0.833 | 0.709 | 0.739 |
| hybrid | 0.975 | 0.817 | 0.855 |
| rerank | 1.000 | 0.983 | 0.986 |
| ablation/bm25_lab | 0.983 | 0.921 | 0.934 |

60 judged queries; nDCG uses binary labels; a random ranking of the 220 documents would get recall@10 near 0.045.
<!-- p2:end own -->

The same scores per query class.

<!-- p2:begin own-classes -->
| System | Metric | mixed (n=15) | identifier (n=13) | paraphrase (n=20) | typo (n=12) |
| --- | --- | ---: | ---: | ---: | ---: |
| bm25 | Recall@10 | 1.000 | 1.000 | 0.950 | 1.000 |
| bm25 | MRR@10 | 1.000 | 0.949 | 0.842 | 0.926 |
| bm25 | nDCG@10 | 0.988 | 0.962 | 0.869 | 0.942 |
| dense | Recall@10 | 1.000 | 0.385 | 0.950 | 0.917 |
| dense | MRR@10 | 0.967 | 0.244 | 0.808 | 0.725 |
| dense | nDCG@10 | 0.970 | 0.278 | 0.843 | 0.773 |
| hybrid | Recall@10 | 1.000 | 0.962 | 1.000 | 0.917 |
| hybrid | MRR@10 | 1.000 | 0.631 | 0.825 | 0.778 |
| hybrid | nDCG@10 | 0.992 | 0.707 | 0.873 | 0.813 |
| rerank | Recall@10 | 1.000 | 1.000 | 1.000 | 1.000 |
| rerank | MRR@10 | 1.000 | 1.000 | 0.975 | 0.958 |
| rerank | nDCG@10 | 0.992 | 1.000 | 0.982 | 0.969 |
| ablation/bm25_lab | Recall@10 | 1.000 | 1.000 | 0.950 | 1.000 |
| ablation/bm25_lab | MRR@10 | 1.000 | 0.910 | 0.867 | 0.926 |
| ablation/bm25_lab | nDCG@10 | 0.989 | 0.933 | 0.888 | 0.942 |
<!-- p2:end own-classes -->

The same scores for the queries you wrote yourself (`hand`) and the ones a model drafted (`claude`), with the difference between the two groups and its interval.
Once both groups have queries, the table also says whether `bm25`'s lead over `dense` differs between them, and what share of each query's content words its best relevant document contains, which is stretch option 6.

<!-- p2:begin own-origins -->
| System | Metric | hand (n=20) | claude (n=40) | hand minus claude | 95% interval | Reading |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| bm25 | Recall@10 | 1.000 | 0.975 | +0.025 | [+0.000, +0.075] | not distinguishable |
| bm25 | MRR@10 | 0.897 | 0.933 | -0.036 | [-0.175, +0.083] | not distinguishable |
| bm25 | nDCG@10 | 0.922 | 0.939 | -0.018 | [-0.127, +0.080] | not distinguishable |
| dense | Recall@10 | 0.800 | 0.850 | -0.050 | [-0.275, +0.150] | not distinguishable |
| dense | MRR@10 | 0.667 | 0.730 | -0.063 | [-0.276, +0.141] | not distinguishable |
| dense | nDCG@10 | 0.701 | 0.757 | -0.056 | [-0.260, +0.140] | not distinguishable |
| hybrid | Recall@10 | 0.925 | 1.000 | -0.075 | [-0.200, +0.000] | not distinguishable |
| hybrid | MRR@10 | 0.720 | 0.866 | -0.146 | [-0.329, +0.026] | not distinguishable |
| hybrid | nDCG@10 | 0.769 | 0.897 | -0.128 | [-0.285, +0.014] | not distinguishable |
| rerank | Recall@10 | 1.000 | 1.000 | +0.000 | [+0.000, +0.000] | not distinguishable |
| rerank | MRR@10 | 0.975 | 0.988 | -0.013 | [-0.075, +0.037] | not distinguishable |
| rerank | nDCG@10 | 0.982 | 0.988 | -0.006 | [-0.052, +0.028] | not distinguishable |
| ablation/bm25_lab | Recall@10 | 1.000 | 0.975 | +0.025 | [+0.000, +0.075] | not distinguishable |
| ablation/bm25_lab | MRR@10 | 0.897 | 0.933 | -0.036 | [-0.174, +0.083] | not distinguishable |
| ablation/bm25_lab | nDCG@10 | 0.922 | 0.940 | -0.018 | [-0.127, +0.079] | not distinguishable |

The hand and claude queries are different queries, so the interval of hand minus claude comes from resampling the queries within each group (10,000 times), not from pairing them.

Do model-written queries favor keyword search? bm25's lead over dense (bm25 minus dense, per query) on the claude queries and on the hand queries, and claude minus hand:

| Metric | Lead on claude | Lead on hand | Claude minus hand | 95% interval | Reading |
| --- | ---: | ---: | ---: | ---: | --- |
| Recall@10 | +0.125 | +0.200 | -0.075 | [-0.300, +0.125] | not distinguishable |
| MRR@10 | +0.203 | +0.231 | -0.027 | [-0.287, +0.225] | not distinguishable |
| nDCG@10 | +0.182 | +0.220 | -0.038 | [-0.279, +0.187] | not distinguishable |

Mean content-word overlap, the share of a query's content words found in its best relevant document: hand 0.86 (20 queries), claude 0.85 (40 queries).
<!-- p2:end own-origins -->

Differences between every pair of systems.

<!-- p2:begin own-pairs -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| dense minus bm25 | Recall@10 | -0.150 | [-0.250, -0.050] | 0.146 | bm25 higher |
| dense minus bm25 | MRR@10 | -0.212 | [-0.332, -0.096] | 0.172 | bm25 higher |
| dense minus bm25 | nDCG@10 | -0.195 | [-0.305, -0.089] | 0.159 | bm25 higher |
| hybrid minus bm25 | Recall@10 | -0.008 | [-0.058, +0.042] | 0.071 | not distinguishable |
| hybrid minus bm25 | MRR@10 | -0.104 | [-0.183, -0.031] | 0.111 | bm25 higher |
| hybrid minus bm25 | nDCG@10 | -0.079 | [-0.147, -0.016] | 0.095 | bm25 higher |
| hybrid minus dense | Recall@10 | +0.142 | [+0.067, +0.233] | 0.125 | hybrid higher |
| hybrid minus dense | MRR@10 | +0.108 | [+0.030, +0.191] | 0.117 | hybrid higher |
| hybrid minus dense | nDCG@10 | +0.116 | [+0.048, +0.190] | 0.102 | hybrid higher |
| rerank minus bm25 | Recall@10 | +0.017 | [+0.000, +0.050] | 0.047 | not distinguishable |
| rerank minus bm25 | MRR@10 | +0.062 | [+0.003, +0.128] | 0.091 | rerank higher |
| rerank minus bm25 | nDCG@10 | +0.052 | [+0.004, +0.107] | 0.075 | rerank higher |
| rerank minus dense | Recall@10 | +0.167 | [+0.083, +0.267] | 0.136 | rerank higher |
| rerank minus dense | MRR@10 | +0.274 | [+0.175, +0.382] | 0.149 | rerank higher |
| rerank minus dense | nDCG@10 | +0.247 | [+0.155, +0.349] | 0.140 | rerank higher |
| rerank minus hybrid | Recall@10 | +0.025 | [+0.000, +0.067] | 0.052 | not distinguishable |
| rerank minus hybrid | MRR@10 | +0.166 | [+0.087, +0.251] | 0.118 | rerank higher |
| rerank minus hybrid | nDCG@10 | +0.131 | [+0.067, +0.200] | 0.096 | rerank higher |
| ablation/bm25_lab minus bm25 | Recall@10 | +0.000 | [+0.000, +0.000] | - | identical on every query |
| ablation/bm25_lab minus bm25 | MRR@10 | +0.000 | [-0.025, +0.025] | 0.033 | not distinguishable |
| ablation/bm25_lab minus bm25 | nDCG@10 | +0.0002 | [-0.018, +0.019] | 0.025 | not distinguishable |
| ablation/bm25_lab minus dense | Recall@10 | +0.150 | [+0.050, +0.250] | 0.146 | ablation/bm25_lab higher |
| ablation/bm25_lab minus dense | MRR@10 | +0.212 | [+0.100, +0.327] | 0.166 | ablation/bm25_lab higher |
| ablation/bm25_lab minus dense | nDCG@10 | +0.195 | [+0.093, +0.302] | 0.154 | ablation/bm25_lab higher |
| ablation/bm25_lab minus hybrid | Recall@10 | +0.008 | [-0.042, +0.058] | 0.071 | not distinguishable |
| ablation/bm25_lab minus hybrid | MRR@10 | +0.104 | [+0.034, +0.180] | 0.107 | ablation/bm25_lab higher |
| ablation/bm25_lab minus hybrid | nDCG@10 | +0.079 | [+0.018, +0.145] | 0.093 | ablation/bm25_lab higher |
| ablation/bm25_lab minus rerank | Recall@10 | -0.017 | [-0.050, +0.000] | 0.047 | not distinguishable |
| ablation/bm25_lab minus rerank | MRR@10 | -0.062 | [-0.129, -0.003] | 0.091 | rerank higher |
| ablation/bm25_lab minus rerank | nDCG@10 | -0.052 | [-0.107, -0.004] | 0.075 | rerank higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time. Two systems that score the same on every query have no interval to speak of, so their MDD is shown as -.
<!-- p2:end own-pairs -->

Which differences are distinguishable and which are not, at your gold-set size?
Do the `hand` queries and the `claude` queries tell the same story?
Did your prediction in `DECISIONS.md` prompt 1 hold?

The distinguishable differences are that rerank is the best system tested, then bm25, then hybrid, and dense is last. Rerank barely beat bm25 with only a +0.06 gain, so rerank is most likely better but cannot be proven based on the results. For recall@10, all of the systems were near 1.0, so nothing can be told from the recall scores.
The hand and claude queries were ranked the same way for both sets, so there is no clear difference. The claude queries did not copy more words then that hand queries, so neither unfairly favored keyword searches. 
I predicted the hybrid would win and bm25 would be the worst in prompt 1, which was incorrect. BM25 beat hybrid and rerank was the best system tested. The reason for this is that my corpus has a lot of identifiers, so keyword search finds them reliably but dense misses them. Dense scored 0.244 on identifiers, which made the hybrid system much worse.

---

## 5. The ablation

Change one thing and keep everything else the same.
Write your hypothesis here before you run it, in one sentence with a direction: "I expect X to raise MRR@10 on my corpus because Y."
The run file for it lives in `runs/own/ablation/`.

I expect changing the bm25's tokenizer to a plain tokenizer will lower MRR@10 for identifier queries because it will split the code into parts that could be shared on multiple notices.

<!-- p2:begin own-ablation -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| ablation/bm25_lab minus bm25 | Recall@10 | +0.000 | [+0.000, +0.000] | - | identical on every query |
| ablation/bm25_lab minus bm25 | MRR@10 | +0.000 | [-0.025, +0.025] | 0.033 | not distinguishable |
| ablation/bm25_lab minus bm25 | nDCG@10 | +0.0002 | [-0.018, +0.019] | 0.025 | not distinguishable |
| ablation/bm25_lab minus dense | Recall@10 | +0.150 | [+0.050, +0.250] | 0.146 | ablation/bm25_lab higher |
| ablation/bm25_lab minus dense | MRR@10 | +0.212 | [+0.100, +0.327] | 0.166 | ablation/bm25_lab higher |
| ablation/bm25_lab minus dense | nDCG@10 | +0.195 | [+0.093, +0.302] | 0.154 | ablation/bm25_lab higher |
| ablation/bm25_lab minus hybrid | Recall@10 | +0.008 | [-0.042, +0.058] | 0.071 | not distinguishable |
| ablation/bm25_lab minus hybrid | MRR@10 | +0.104 | [+0.034, +0.180] | 0.107 | ablation/bm25_lab higher |
| ablation/bm25_lab minus hybrid | nDCG@10 | +0.079 | [+0.018, +0.145] | 0.093 | ablation/bm25_lab higher |
| ablation/bm25_lab minus rerank | Recall@10 | -0.017 | [-0.050, +0.000] | 0.047 | not distinguishable |
| ablation/bm25_lab minus rerank | MRR@10 | -0.062 | [-0.129, -0.003] | 0.091 | rerank higher |
| ablation/bm25_lab minus rerank | nDCG@10 | -0.052 | [-0.107, -0.004] | 0.075 | rerank higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time. Two systems that score the same on every query have no interval to speak of, so their MDD is shown as -.
<!-- p2:end own-ablation -->

The queries your ablation helped and hurt, against the system it varies, by reciprocal rank.
`p2 score` finds that system from a line such as `BASE = "bm25"` in your variant's file, or else from its name: `bm25_lab` varies `bm25`.

<!-- p2:begin own-ablation-queries -->
ablation/bm25_lab against bm25 (BASE = "bm25" in p2/retrievers/bm25_lab.py): it helped 1 queries, hurt 1 and left 58 unchanged.

| Query | Class | Origin | bm25 RR | ablation/bm25_lab RR | Change | Effect |
| --- | --- | --- | ---: | ---: | ---: | --- |
| c28 | paraphrase | claude | 0.500 | 1.000 | +0.500 | helped |
| c00 | identifier | claude | 1.000 | 0.500 | -0.500 | hurt |

RR is the reciprocal rank of the first relevant document in the top 10 (0 when none is there), the per-query value behind MRR@10; the queries at the top of each list are the ones to read.
<!-- p2:end own-ablation-queries -->

What did you change, what happened, and does the interval support the claim you want to make?
If the result is not distinguishable, say what size of effect your gold set could have seen.
Read the queries at the top of each list in the second table, and say whether your change explains them.

I changed the bm25 tokenizer from one that keeps codes whole to one that splits them into pieces. Almost nothing changed in the tests, only 2 queries had different results. c00 is an identifier search for ANSI/ANS-8.1, and the plain tokenizer split the search into ANSI, ANS, 8, 1. This found another notice and ranked it higher than the correct one. This only happened on this query because most of my queries are still unique even when split, so most stayed the same. 
c28 changed as well, but its a plain english question and my change does not explain why this one changed.
The interval does not support my claim. There was almost no change in the results, so if there is an effect, it is smaller than the minimum my queries would be able to see (0.03 MRR@10).

---

## 6. Failure analysis

Pick the queries where your best system on your own corpus failed: the relevant document is missing from the top 10, or sits far below the top.
Take at least five, and read what the system returned next to what was relevant.
Then sort the failures by cause, for example a vocabulary mismatch, near-duplicate documents, a chunk that cut the answer in half, a query that is ambiguous, or a label that was wrong, because sometimes the gold set is what failed.

| qid | what the best system returned | what was relevant | cause | what you would try |
|---|---|---|---|---|
| h08 | ml101970221 | ml102160735 | The gold set is too narrow, as both talk about updated probabilistic seismic hazards, which was the query. | Add this notice to the gold set and rerun the tests on all systems |
| c39 | ml071220351 | ml080440014 | The gold set is too narrow, both of these notices talk about fires on diesel generator exhaust pipes. | Add this notice to the gold set and rerun the tests on all systems | 
| c38 | ml081850581 | ml080370453 | The vocabulary used in the query was not exact wording from the document | The relevant document did not say 'public websites' directly, so this is a limitation of the bm25 system. | If the gold set had queries with exact wording, bm25 would be able to pick the relevant document more easily. | 
| h09 | ml031830015 | ml092510055 | the only relevant words was 'User's', but the query said 'users', and 'manual' | This was a typo query, and bm25 does not have a way to check for similar words. | This is a limitation of bm25, so the only thing I could try would be to optimize the queries for the system |
| h16 | ml101670005 | ml093340392 | bm25 matched the individual words in the date, instead of the whole date 'February 26, 2010. | This is a limitation of bm25, so the only thing I could try would be to optimize the queries for the system | 

My best system (rerank) only had two failures, and both were failures of the gold set. The returned notices were both correct, and I would add them to the gold set.
To get to the required 5 failures, I used 3 from the second best system (bm25). These failures were caused by a typo which bm25 does not have a way to reason about finding similar words, and from the query not using exact wording from the document.

---

## 7. Cross-corpus comparison

The two tables to compare are the shared-corpus scores in section 1 and your own-corpus scores in section 4, with their intervals.
If you want them side by side, copy the rows you need into a table here and say that you copied them.

Did the winner change between the shared corpus and yours?
Why, or why not: what is different about the two collections (document length, vocabulary, identifiers, near-duplicates, how the queries were written), and which of your explanations did you test and which are guesses?
Say what 20 queries on one side and your gold-set size on the other cannot support.

The winner did not change between the shared corpus and my corpus, but the rest did change. On the shared corpus, none of dense, hybrid, and bm25 was distinguishable. On my corpus, bm25 beat dense (+0.212) and hybrid (+0.104), and hybrid beat dense all with intervals above 0. rerank's lead over bm25 was also much smaller on my corpus (+0.06) than the shared corpus (+0.29). (measured)

I think the main reason the results were much different on the two corpora is my gold set. The shared gold set paraphrases were written to not include words the document used, and bm25 got a 0.000 on recall. However, I wrote mine from the documents, which is probably the main reason bm25 did so well on my corpus (measured). 
I also had claude measure the document lengths, and the shared corpus had a median length of 68 words while my corpus's median was 1650 words. I am not sure what effect this has, but it is a large difference. (guess)
My queries and Claude's queries were measured to have almost the same overlap and no distinguishable difference in any system, so the hand and claude queries had no detectable difference. (measured)

The 20 queries on the shared corpus can only detect differences of 0.167 to 0.42, and my 60 queries can distinguish gaps from 0.09 to 0.17. The shared corpus gold set size is why all of the systems are not distinguishable besides rerank, and my gold set is why I can barely distinguish between rerank vs bm25, which has a gap of +0.06 but the entire interval is above 0.

---

## 8. Stretch

498E: the stretch is one of the six options in the brief's "One stretch" section, and that section says what earns the 25 points for each.
It is optional, so `uv run p2 check --final` never waits on this section.
598E: the rider is your stretch, so write "rider" below and put its results in section 9; the other options add no points, because the project is capped at 150.

Whichever option you chose, write these five things:

1. The option's name.
2. What you did, and the files that hold it.
3. The table `p2 score` wrote for it, by name: one of the three below, `own-ablation` and `own-ablation-queries` in section 5 for a second ablation, `own-origins` in section 4 for the hand and claude queries, or `repeats` in section 9 for the rider.
4. What its interval lets you claim, and what it does not.
5. One thing you would do next, and what result would tell you it worked.

For a second ablation, write its hypothesis here before you run it, and commit it, so your history shows that it came first.
For the hand and claude queries, do the same with your prediction before you score.

### Claim-level faithfulness check (option 2)

Claude's verdicts from `p2 judge` against your own verdicts in the calibration file.

<!-- p2:begin stretch-judge -->
_No judged answers yet (stretch option 2): `uv run p2 judge answers/shared/LABEL.json` writes them, your own verdicts go in answers/shared/LABEL.calibration.tsv, and then `uv run p2 score` fills this table._
<!-- p2:end stretch-judge -->

### Cost and latency (option 3)

The Claude calls, tokens and seconds in every trace you committed, and what a cheaper system or answers file saves against what it loses.

<!-- p2:begin stretch-cost -->
Every trace in traces/ that records a Claude call:

| Trace | System | Spans | Claude calls | Saved | Input tokens | Output tokens | Seconds | Input per span | Output per span | Seconds per span |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| traces/answers-rerank.jsonl | rerank | 12 | 24 | 4 | 261,353 | 4,233 | 78.8 | 21,779 | 353 | 6.6 |
| traces/answers-rerank.r1.jsonl | rerank | 12 | 24 | 0 | 248,821 | 4,106 | 79.3 | 20,735 | 342 | 6.6 |
| traces/answers-rerank.r2.jsonl | rerank | 12 | 24 | 0 | 264,035 | 4,571 | 82.3 | 22,003 | 381 | 6.9 |
| traces/answers-rerank.r3.jsonl | rerank | 12 | 24 | 0 | 284,067 | 4,484 | 84.1 | 23,672 | 374 | 7.0 |
| traces/own-own-rerank.jsonl | rerank | 60 | 60 | 3 | 1,205,201 | 5,460 | 260.6 | 20,087 | 91 | 4.3 |
| traces/shared-practice-rerank.jsonl | rerank | 20 | 20 | 1 | 278,796 | 2,023 | 57.6 | 13,940 | 101 | 2.9 |
| traces/shared-practice-rerank.r1.jsonl | rerank | 20 | 20 | 0 | 311,590 | 2,040 | 59.9 | 15,580 | 102 | 3.0 |
| traces/shared-practice-rerank.r2.jsonl | rerank | 20 | 20 | 0 | 314,765 | 2,042 | 62.5 | 15,738 | 102 | 3.1 |
| traces/shared-practice-rerank.r3.jsonl | rerank | 20 | 20 | 0 | 313,430 | 1,930 | 63.9 | 15,672 | 96 | 3.2 |
| traces/shared-test-rerank.jsonl | rerank | 40 | 40 | 0 | 586,809 | 3,755 | 123.5 | 14,670 | 94 | 3.1 |

A span is one query of a run, one question of an answers file, or one claim of a judged file. A saved reply costs nothing now, so it counts the tokens and the seconds of the call that made it.

Every pair of systems on the same queries where at least one calls Claude, the one with fewer Claude input tokens per query first:

| Cheaper minus dearer | Queries | MRR@10 difference | 95% interval | Input tokens saved per query | Seconds saved per query | Reading |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| shared practice: bm25 minus rerank | 20 | -0.293 | [-0.533, -0.043] | 13,940 | 2.9 | rerank higher |
| shared practice: dense minus rerank | 20 | -0.237 | [-0.408, -0.083] | 13,940 | 2.9 | rerank higher |
| shared practice: hybrid minus rerank | 20 | -0.329 | [-0.504, -0.164] | 13,940 | 2.9 | rerank higher |
| own: bm25 minus rerank | 60 | -0.062 | [-0.128, -0.003] | 20,087 | 4.3 | rerank higher |
| own: dense minus rerank | 60 | -0.274 | [-0.382, -0.175] | 20,087 | 4.3 | rerank higher |
| own: hybrid minus rerank | 60 | -0.166 | [-0.251, -0.087] | 20,087 | 4.3 | rerank higher |

The difference is the cheaper system's score minus the dearer one's, with its paired interval; the savings count Claude calls only, so a system that makes none saves all of the other's.

Systems that do not call Claude, from traces/retrieval/ on the machine that last ran `p2 score` (git ignores that folder, so `p2 check` does not compare this part):

| Trace | System | Queries | Seconds | Milliseconds per query |
| --- | --- | ---: | ---: | ---: |
| traces/retrieval/own-own-ablation-bm25_lab.jsonl | bm25_lab | 60 | 0.04 | 0.7 |
| traces/retrieval/own-own-bm25.jsonl | bm25 | 60 | 0.04 | 0.7 |
| traces/retrieval/own-own-dense.jsonl | dense | 60 | 2.11 | 35.1 |
| traces/retrieval/own-own-hybrid.jsonl | hybrid | 60 | 2.41 | 40.1 |
| traces/retrieval/shared-practice-bm25.jsonl | bm25 | 20 | 0.04 | 1.8 |
| traces/retrieval/shared-practice-dense.jsonl | dense | 20 | 0.84 | 41.9 |
| traces/retrieval/shared-practice-hybrid.jsonl | hybrid | 20 | 1.34 | 66.9 |
| traces/retrieval/shared-test-bm25.jsonl | bm25 | 40 | 0.07 | 1.8 |
| traces/retrieval/shared-test-dense.jsonl | dense | 40 | 1.67 | 41.8 |
| traces/retrieval/shared-test-hybrid.jsonl | hybrid | 40 | 2.15 | 53.9 |
<!-- p2:end stretch-cost -->

### The grep agent (option 5)

Your stretch run on some of your own queries against the four systems on the same queries.

<!-- p2:begin stretch-agent -->
_No stretch runs yet (stretch option 5): `uv run p2 run --corpus own --queries eval/own/agent.queries.tsv --system agent --stretch` writes one to runs/own/stretch/, then `uv run p2 score` fills this table._
<!-- p2:end stretch-agent -->

### Your stretch

1. The option's name.
   Rider
2. What you did, and the files that hold it.
   I did three more runs of reranker on the 20 practice queries, the files are runs/shared/rerank.practice.<r1, r2, r3>.trec.
   There are also three more answer files: answers/shared/rerank.<r1, r2, r3>.json.
   Traces: traces/shared-practice-rerank.<r1, r2, r3>.jsonl and traces/answers-rerank.<r1, r2, r3>.jsonl.
3. The table `p2 score` wrote for it, by name: one of the three below, `own-ablation` and `own-ablation-queries` in section 5 for a second ablation, `own-origins` in section 4 for the hand and claude queries, or `repeats` in section 9 for the rider.
   repeats, own-pairs
4. What its interval lets you claim, and what it does not.
   Claims
   The three repeats have a spread of 0.000 and the gain over hybrid on the practice queries was +0.329 on every run, so the gain survives rerunning Claude.
   On my corpus, rerank minus hybrid is +0.166 and the interval is above 0, so this is distinguishable.
   Cannot be claimed
   I cannot claim that Claude is deterministic, so these three runs do not mean that all runs will agree.
   I cannot claim that the 8 out of 8 verified and 4 out of 4 declines are guaranteed. The intervals are [0.676, 1.000] and [0.510, 1.000].
   I cannot claim that the true gap is at least 0.15, the lower end of the interval is 0.087.

5. One thing you would do next, and what result would tell you it worked.
   I would fix the labels for h08 and c39 and rescore all systems. It worked if the rerank minus hybrid interval stays above 0 and rerank's MRR@10 goes closer to 1.0.
    

---

## 9. 598E only - repeats and the pre-registered claim

498E students can leave this section as it is; nothing checks it.
598E students replace each line that starts with "598E: write", and `uv run p2 check --final` counts those lines as work still to do until they are gone.

### Repeats on the shared corpus

Three runs of the reranker on the practice queries, and three answers files, with their run-to-run spread and Wilson intervals.

<!-- p2:begin repeats -->
Repeated runs of rerank on shared/practice:

| Run | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| rerank.r1 | 0.758 | 0.800 | 0.769 |
| rerank.r2 | 0.758 | 0.800 | 0.769 |
| rerank.r3 | 0.758 | 0.800 | 0.769 |
| range (max minus min) | 0.000 | 0.000 | 0.000 |

| Comparison | Metric | Mean difference | 95% interval | Reading |
| --- | --- | ---: | ---: | --- |
| rerank.r1 minus hybrid | Recall@10 | +0.167 | [+0.058, +0.292] | rerank.r1 higher |
| rerank.r2 minus hybrid | Recall@10 | +0.167 | [+0.058, +0.292] | rerank.r2 higher |
| rerank.r3 minus hybrid | Recall@10 | +0.167 | [+0.058, +0.292] | rerank.r3 higher |
| rerank.r1 minus hybrid | MRR@10 | +0.329 | [+0.164, +0.504] | rerank.r1 higher |
| rerank.r2 minus hybrid | MRR@10 | +0.329 | [+0.164, +0.504] | rerank.r2 higher |
| rerank.r3 minus hybrid | MRR@10 | +0.329 | [+0.164, +0.504] | rerank.r3 higher |
| rerank.r1 minus hybrid | nDCG@10 | +0.325 | [+0.199, +0.453] | rerank.r1 higher |
| rerank.r2 minus hybrid | nDCG@10 | +0.325 | [+0.199, +0.453] | rerank.r2 higher |
| rerank.r3 minus hybrid | nDCG@10 | +0.325 | [+0.199, +0.453] | rerank.r3 higher |

Repeated answers shared/rerank:

| File | Verified (in) | 95% interval | Declined (out) | 95% interval |
| --- | ---: | ---: | ---: | ---: |
| rerank.r1 | 8 of 8 (100%) | [0.676, 1.000] | 4 of 4 (100%) | [0.510, 1.000] |
| rerank.r2 | 8 of 8 (100%) | [0.676, 1.000] | 4 of 4 (100%) | [0.510, 1.000] |
| rerank.r3 | 8 of 8 (100%) | [0.676, 1.000] | 4 of 4 (100%) | [0.510, 1.000] |
| range (max minus min) | 0.000 |  | 0.000 |  |

Each repeat answers the same questions, so the repeats are not independent trials and their counts are not pooled into one interval.
<!-- p2:end repeats -->

Does the reranker's gain over its first stage survive the run-to-run variation?
Write what the spread is, how it compares with the gain, and what the Wilson intervals on the verified share and the declined share say about 8 and 4 questions.

The spread was 0.000 on all three metrics, so they did survive the run-to-run variation. 
The gain for rerank minus hybrid is +0.329 MRR@10, interval [+0.164, +0.504] and was the same on every repeat, meaning Claude did not threaten the results.
Wilson Intervals:
Verified 8 of 8, [0.676, 1.000]. With only 8 questions, the rate could be as low as about 68%.
Declined 4 out of 4, [0.510, 1.000]. With only 4 questions, the rate could be as low as 51%.
This is a very small sample, so the results do not prove that the system never fails.


### The pre-registered claim

The claim, the smallest effect, the gold-set size and the test are in `PREREG.md`, committed before your own gold-set judgments.
Here, say whether you followed the plan, what the interval turned out to be, and what that means.
The outcome section of `PREREG.md` holds the short version.

Yes, PREREG sections 1-4 were committed before my first judgment. I wrote 20 hand queries and claude wrote 40, so there were 60 queries total. I predicted the Δ would be 0.15 for rerank minus hybrid MRR@10. The interval was +0.166 [0.087, 0.251]. This interval is entirely above 0 in the direction I predicted, so the PREREG claim is supported.
My gold set size was big enough to see Δ of 0.15 because p2 score printed MDD scores below 0.15.
The difference is distinguishable from zero, and the estimate of 0.166 is above 0.15. However, the lower end of the interval was 0.087, so I cannot claim the gap is at least 0.15.
Rerank had two misses, but they were failures of the gold set, not the system. The top result returned should have been a result in the gold set for both, so fixing the gold set could widen the gap.