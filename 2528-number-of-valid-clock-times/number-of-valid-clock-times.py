class Solution:
    def countTime(self, time: str) -> int:
        res = 1
        if time[:2] == "??": res*=24
        else:
            if time[0] == '?':
                if time[1] <='3': res*=3
                else: res*=2
            elif time[1] == '?':
                if time[0] <='1': res*=10
                else: res*=4
        
        if time[3:] == "??": res*=60
        else:
            if time[3] == '?':
                res*=6
            elif time[4] == '?':
                res*=10
        return res