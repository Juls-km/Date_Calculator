class DateCalculator:
    def __init__(self, year, month, day):
        self.original_year = year
        self.original_month = month
        self.day = day

      
        if month <= 2:
            self.month = month + 12
            self.year = year - 1
        else:
            self.month = month
            self.year = year

        self.K = self.year % 100         
        self.J = self.year // 100        

    def calculate_weekday(self):
        q = self.day
        m = self.month
        K = self.K
        J = self.J

        h = (q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) + 5 * J) % 7

       
        weekdays = [
            "Saturday", "Sunday", "Monday", "Tuesday",
            "Wednesday", "Thursday", "Friday"
        ]

        return weekdays[h]


date = DateCalculator(1589, 9, 15)  
weekday = date.calculate_weekday()
print(f"September 15, 1589 was a {weekday}.")
