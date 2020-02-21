d1 = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', \
    10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', \
    17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}

d2 = {20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70:'Seventy', 80: 'Eighty', 90: 'Ninety'}

class Solution:
    def numberToWords(self, num: int) -> str:
        if num < 20:
            return d1[num]
        elif num < 100:
            tens, rem = divmod(num, 10)
            t, r = d2[tens*10], self.numberToWords(rem) 
            return t + ' ' + r if rem > 0 else t 
        elif num < 1000:
            hundreds, rem = divmod(num, 100)
            h, r = d1[hundreds] + ' Hundred', self.numberToWords(rem) 
            return h + ' ' + r if rem > 0 else h 
        elif num < 10**6:
            thousands, rem = divmod(num, 1000)
            t = self.numberToWords(thousands) + ' Thousand'
            r = self.numberToWords(rem) 
            return t + ' ' + r if rem > 0 else t 
        elif num < 10**9:
            millions, rem = divmod(num, 10**6)
            m = self.numberToWords(millions) + ' Million'
            r = self.numberToWords(rem) 
            return m + ' ' + r if rem > 0 else m 
        elif num < 10**12:
            billions, rem = divmod(num, 10**9)
            b = self.numberToWords(billions) + ' Billion'
            r = self.numberToWords(rem) 
            return b + ' ' + r if rem > 0 else b 
                
