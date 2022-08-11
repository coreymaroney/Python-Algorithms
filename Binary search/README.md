This script has 2 implementations of binary search, one is to visualize a mistake I found within Michael Sambol's (@msambol) "Binary search in 3 minutes" implementation.

The discrepancy I discovered is between Sambol's visualization and his implementation, so he has committed a fix to his repository to address the problem. 
While the error is simple, his visualization rounds up, but his algorithm rounds down. 
- Rounding up is math.ceil((right + left) / 2). — only one slash
- Rounding down is (right + left) // 2.
