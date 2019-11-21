class Solution:
    def restoreIpAddresses(self, ip: str) -> List[str]:
        
        self.solutions: List[str] = []
        
        def dfs(idx: int, restored: str, count: int):
                    
            if count > 4:
                return
            
            if count == 4 and idx == len(ip):
                self.solutions +=  [restored]
            
            for i in range(4):
                if idx + i > len(ip): 
                    break
                s = ip[idx:idx+i+1]
                
                if s and int(s) >= 256 or (len(s) > 1 and s[0] == '0'): continue
                    
                if count == 3:
                    dfs(idx+i+1, restored+s, count + 1)
                else:
                    dfs(idx+i+1, restored+s+'.', count+1)
            
        dfs(0, '', 0)
        
        return self.solutions