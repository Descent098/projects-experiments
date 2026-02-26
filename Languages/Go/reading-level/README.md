# Readn

...


## Warning

The effectiveness of this library is massively limited by it's accuracy in counting certain values in particular counting sentences, and sylables.

## AutomatedReadabilityIndex (ARI)

...

The index is basically `index-1` years of education to read. So

| Score | Age | Grade Level |
|-------|-----|-------------|
| 1 | 5-6 | Kindergarten |
| 2 | 6-7 | First Grade |
| 3 | 7-8 | Second Grade |
| 4 | 8-9 | Third Grade |
| 5 | 9-10 | Fourth Grade |
| 6 | 10-11 | Fifth Grade |
| 7 | 11-12 | Sixth Grade |
| 8 | 12-13 | Seventh Grade |
| 9 | 13-14 | Eighth Grade |
| 10 | 14-15 | Ninth Grade |
| 11 | 15-16 | Tenth Grade |
| 12 | 16-17 | Eleventh Grade |
| 13 | 17-18 | Twelfth Grade |
| 14+ | 18-22 | College/University |


This one is slightly more accurate than the other two algorithms because it does not rely on sylables, opting for character count, which is trivial to do. This means the error % is just dependent on sentence count accuracy. It is also designed specifically for technical documents, and works best in this context, though it also works for more general use cases.




## Simple Measure Of Gobbledygook (SMOG)

**Does not work on text with less than 30 sentences**



## References

- https://en.wikipedia.org/wiki/Automated_readability_index
- https://en.wikipedia.org/wiki/SMOG

