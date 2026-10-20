class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        curr,res = [],[]


        def dfs(openC,closeC):
            if n == openC == closeC:
                res.append(''.join(curr))
                return


            if openC < n:
                curr.append('(')
                dfs(openC+1,closeC)
                curr.pop()

            if closeC < openC:
                curr.append(')')
                dfs(openC,closeC+1)
                curr.pop()

            



        dfs(0,0)
        return res