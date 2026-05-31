class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        child_ptr = 0
        cookie_ptr = 0
        
        while child_ptr < len(g) and cookie_ptr < len(s):
            if s[cookie_ptr] >= g[child_ptr]:
                child_ptr += 1

            cookie_ptr += 1

        return child_ptr
    
    def lemonadeChange(self, bills: List[int]) -> bool:
        five,ten=0,0
        for i in range(len(bills)):
            if bills[i]==5:
                five+=1
            elif bills[i]==10:
                if five>0:
                    five-=1
                    ten+=1
                else:
                    return False
            else:
                if five>0 and ten>0:
                    five-=1
                    ten-=1
                elif five>=3:
                    five-=3
                else:
                    return False
                
        return True
    
    def canJump(self, nums: List[int]) -> bool:
        maxlen,leng=0,0

        for i in range(len(nums)):
            if i>maxlen:     # acnt just loop on all
                return False
            
            maxlen=max(maxlen,i+nums[i])

            if maxlen>=len(nums)-1:
                return True
            
        return maxlen>=len(nums)-1

    def jump(self, nums: List[int]) -> int:
        jump,maxlen=0,0
        l,r=0,0

        while r<len(nums)-1:
            for i in range(l,r+1):
                maxlen=max(maxlen,nums[i]+i)
            l=r+1
            r=maxlen
            jump+=1

        return jump

