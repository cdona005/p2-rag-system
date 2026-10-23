# Decision log

Your methods section, in your own words.
About one to two pages in total.

Answer these as you go, not the night before it is due.
Each answer is easier to write while the decision is still fresh, and prompt 1 only works if you write it before you see your own-corpus numbers.
Specifics beat polish: a short, honest answer with a number in it is worth more than a long vague one.

Each prompt ends with a marker line.
Replace that line with your answer.
`uv run p2 check` reports a marker as unfinished work, and `uv run p2 check --final` fails while any marker is left, so a finished log is part of being done.

Please do not let the agent write these for you.
These answers are about what you chose and what you knew, and the agent cannot know that.
Prompt 3 in particular only works in your own words.

---

## 1. Why this corpus, and what you expected

Why did you pick the corpus you used in stage 2, and why does it belong to a field or a question you care about?
Then say what you expected before you measured anything: which of `bm25`, `dense`, `hybrid` and `rerank` do you think will win on it, and which will do worst, and why?

Commit this answer before your first `uv run p2 score` on the own corpus.
Git history then shows that the expectation came first, which is what lets it be wrong in a way that teaches you something.
If you were surprised later, say so in prompt 4 or in EVAL.md; do not come back and rewrite this one.

I chose NRC Information Notices, 2003–2010 for my corpus because it is about commercial nuclear power and medical problems that have been found in plants, and I was a nuclear mechanic in the Navy for 8 years, so I have read similar documents and understand what they are saying.

I think the hybrid system will win because when searching this document, there will be a lot of repeat words and phrases that will not all be applicable to the search, but a bm25 retriever will find all occurences of the phrase, such as CRDM (control rod drive mechanism). The hybrid will then use a dense system to examine context and compare to bm25, which should find more accurate top results. I think the bm25 system will be the worst because there are no definitions or phrases that only apply to one topic, many of the same phrases in this document will be repeated in many different contexts.

---

## 2. A fork in the road

Name one real design choice where you could have gone two ways: the chunk size, the embedding model, how the two systems are fused, how many documents the reranker sees, a sentence in `prompts/answer.txt`, how you cleaned the corpus.

Say which you picked, what the alternative was, and what you gave up by not taking it.
If you measured both, give both numbers.
If you rejected the alternative without measuring it, say why that was a fair call, and what it cost you in time, tokens or complexity.

"There was no alternative" is not an answer.
Find the fork.

When working on the dense rag system, the prefix is "" by default, and I wanted to see if adding a prefix would help. I had Claude test adding "Represent this sentence for searching relevant passages: " When testing, there was not a detectable difference between having no query prefix vs adding one. Since adding a prefix did not change the results, I decided not to add the prefix. The table below shows the difference in runs.
Overall, prefix minus none:


| Metric | Difference | 95% interval |
| -------- | -------- | -------- |
| MRR@10 | −0.028 | −0.108 to +0.035 |
| nDCG@10 | +0.013 | −0.020 to +0.042 |
| recall@10 | +0.029 | 0.000 to +0.075 |

---

## 3. Where you overruled the agent

One time Claude suggested, wrote or claimed something and you did not take it.
It might be a relevance judgment you disagreed with, a retriever it called finished when a run file showed otherwise, a number it summarized wrongly, or a license it said was fine.

What did it do?
How did you notice?
What did you do instead?

If it genuinely never happened, say so plainly, and then say what you would have had to check in order to notice.
Being honest here costs you far less than a story you cannot defend when you record your video.

One time I overruled the agent is when writing the eval document, Claude kept telling me I had to put information that was not relevant to the question. An example is when Claude said that I had to write 60 queries by hand based on my PREREG, but it clearly says that there are 60 queries total and I will write 20 by hand and Claude will write 40. I corrected the model and made it reread the PREREG file to move on with the testing, as it kept saying I had to write 40 more queries before I could test. 

---

## 4. A number you do not trust

Pick one number in `EVAL.md` that you do not fully trust, and say why.
It could be a mean over a small query class, a difference whose interval includes zero, a verified share of 100%, a score on a gold set you wrote yourself, or a result you got only once.

What would have to be true for you to trust it?
Did you do anything to test it, and what did that show?

One number in EVAL.md that I do not trust is the rerank MRR@10 score of .983. This is at the ceiling, and if my gold set was correct, it would have gotten closer to a 1.0. This seems very high for any system, so I think my gold set might have been too easy. 

For me to trust it, I would have to add some harder questions to my gold set and see if the score changes. If it does not, then the score is accurate, but I think the score would lower.

I tested this and the rescore for rerank MRR@10 was 1.0. I discarded these result so I did not have to change all of the numbers in my report, but this shows that the gold set being corrected would have given rerank for MRR@10 1.0.

---

## 5. What is still wrong

One thing in your system, your corpus or your gold set that is not right, not finished, or that you do not fully understand.

What would you do next, and how would you find out whether it matters?
Name the file, the query or the document where someone could look.

My gold set has two questions that did not include the documents rerank returned, but those documents should have been included in the gold set. The documents were very similar to the ones I had marked correct, so rerank should have gotten a higher score. The questions are h08 and c39, and the judgements are in eval/own/qrels.txt. The queries are in eval/own/queries.tsv, and eval.md section 6 has the failure table. 
To fix this, I would add these documents into the gold set judgements and rerun all systems on the new gold set. To see if this matters, I would check that rerank's score gets close to 1.0 and picks these documents correctly.