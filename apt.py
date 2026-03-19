from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'TCS NQT 2026: 100 Most Important Aptitude Problems with Solutions', 0, 1, 'C')
        self.ln(5)
    
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')
    
    def chapter_title(self, title):
        self.set_font('Arial', 'B', 11)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 8, title, 0, 1, 'L', 1)
        self.ln(3)
    
    def chapter_body(self, body):
        self.set_font('Arial', '', 9)
        self.multi_cell(0, 5, body)
        self.ln(3)

# Create PDF
pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# Title
pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, 'TCS NQT 2026: 100 Most Important Aptitude Problems', 0, 1, 'C')
pdf.set_font('Arial', 'I', 9)
pdf.cell(0, 8, 'With Detailed Solutions - Based on Previous Year Patterns', 0, 1, 'C')
pdf.ln(10)

# Questions data
questions = [
    # Section 1: Number System & Divisibility (1-5)
    ("Section 1: Number System & Divisibility (1-5)", [
        ("1. Find the unit digit of 3^65 x 6^59 x 7^71.", "Answer: 4\nSolution: Unit digit of 3^65 (cycle 4, rem 1) = 3. Unit digit of 6^59 = 6. Unit digit of 7^71 (cycle 4, rem 3) = 3. Product: 3 x 6 x 3 = 54 -> Unit digit = 4."),
        ("2. What is the remainder when 17^200 is divided by 18?", "Answer: 1\nSolution: 17 ≡ -1 (mod 18). So, (-1)^200 = 1. Remainder is 1."),
        ("3. How many zeros are at the end of the product 1 x 5 x 10 x ... x 60?", "Answer: 14\nSolution: Series has 12 terms (multiples of 5). Count factors of 5: 1+1+1+1+2+1+1+1+1+2+1+1 = 14. Factors of 2 are sufficient. Zeros = 14."),
        ("4. Find the largest 4-digit number divisible by 12, 15, and 18.", "Answer: 9900\nSolution: LCM(12,15,18) = 180. 9999 ÷ 180 gives remainder 99. Required number = 9999 - 99 = 9900."),
        ("5. If the number 517*324 is divisible by 3, what is the smallest whole number in place of *?", "Answer: 2\nSolution: Sum of digits = 22 + *. For divisibility by 3, 22+* must be divisible by 3. Smallest * is 2 (22+2=24)."),
    ]),
    
    # Section 2: LCM & HCF (6-10)
    ("Section 2: LCM & HCF (6-10)", [
        ("6. The LCM of two numbers is 4800 and their HCF is 160. If one number is 480, find the other.", "Answer: 1600\nSolution: Product of numbers = LCM × HCF. 480 × x = 4800 × 160. x = (4800 × 160) / 480 = 1600."),
        ("7. Three bells toll at intervals of 12, 15, and 18 minutes. If they toll together at 9 AM, when will they toll together again?", "Answer: 12 PM\nSolution: LCM(12,15,18) = 180 minutes = 3 hours. 9 AM + 3 hours = 12 PM."),
        ("8. Find the HCF of 2/3, 4/9, 6/5.", "Answer: 2/45\nSolution: HCF of fractions = HCF(Numerators) / LCM(Denominators). HCF(2,4,6)=2. LCM(3,9,5)=45. Result = 2/45."),
        ("9. Find the least number divisible by 12, 18, 21, 30.", "Answer: 1260\nSolution: LCM(12,18,21,30) = 1260."),
        ("10. The HCF of two numbers is 11 and their LCM is 7700. If one number is 275, find the other.", "Answer: 308\nSolution: 275 × x = 11 × 7700. x = (11 × 7700) / 275 = 308."),
    ]),
    
    # Section 3: Ratio & Proportion (11-15)
    ("Section 3: Ratio & Proportion (11-15)", [
        ("11. If A:B = 2:3 and B:C = 4:5, find A:B:C.", "Answer: 8:12:15\nSolution: Make B common. LCM(3,4)=12. A:B = 8:12, B:C = 12:15. So A:B:C = 8:12:15."),
        ("12. Rs. 700 is divided among A, B, C such that A gets half of what B gets and B gets half of what C gets. Find C's share.", "Answer: Rs. 400\nSolution: A = B/2, B = C/2 → A = C/4. Ratio A:B:C = 1:2:4. Total parts = 7. C's share = (4/7) × 700 = 400."),
        ("13. Two numbers are in the ratio 3:5. If 9 is subtracted from each, the ratio becomes 12:23. Find the smaller number.", "Answer: 33\nSolution: (3x-9)/(5x-9) = 12/23. 69x - 207 = 60x - 108. 9x = 99 → x = 11. Smaller number = 3x = 33."),
        ("14. If x:y = 3:4, find (4x+5y):(5x-2y).", "Answer: 32:7\nSolution: Substitute x=3, y=4. (12+20):(15-8) = 32:7."),
        ("15. The ratio of incomes of A and B is 5:4 and expenditures is 3:2. If each saves Rs. 800, find A's income.", "Answer: Rs. 2000\nSolution: Income 5x, 4x. Exp 3y, 2y. 5x-3y=800, 4x-2y=800. Solve: x=400. A's Income = 5×400 = 2000."),
    ]),
    
    # Section 4: Percentages (16-20)
    ("Section 4: Percentages (16-20)", [
        ("16. If A's salary is 25% more than B's, by what percent is B's salary less than A's?", "Answer: 20%\nSolution: Let B=100, A=125. Diff=25. % less = (25/125) × 100 = 20%."),
        ("17. A number is increased by 20% and then decreased by 20%. What is the net change?", "Answer: 4% Decrease\nSolution: 100 → 120 → 120 - 24 = 96. Net change = 4% decrease. Formula: -(x²/100) = -4%."),
        ("18. In an exam, 35% failed in Hindi, 45% failed in English, and 20% failed in both. Find the % who passed in both.", "Answer: 40%\nSolution: Failed in either = 35 + 45 - 20 = 60%. Passed in both = 100 - 60 = 40%."),
        ("19. The population of a town is 10,000. It increases by 10% annually. What will be the population after 2 years?", "Answer: 12,100\nSolution: 10000 × (1.1)² = 10000 × 1.21 = 12100."),
        ("20. If 20% of a number is 120, what is 120% of that number?", "Answer: 720\nSolution: Number = 120 / 0.2 = 600. 120% of 600 = 1.2 × 600 = 720."),
    ]),
    
    # Section 5: Averages (21-25)
    ("Section 5: Averages (21-25)", [
        ("21. The average of 5 numbers is 27. If one number is excluded, the average becomes 25. Find the excluded number.", "Answer: 35\nSolution: Sum of 5 = 5×27 = 135. Sum of 4 = 4×25 = 100. Excluded = 135 - 100 = 35."),
        ("22. The average age of 10 students is 15 years. If the teacher's age is included, the average increases by 1 year. Find the teacher's age.", "Answer: 26 years\nSolution: Total age students = 150. New average 16 for 11 people = 176. Teacher = 176 - 150 = 26."),
        ("23. Find the average of the first 50 natural numbers.", "Answer: 25.5\nSolution: Average = (n+1)/2 = 51/2 = 25.5."),
        ("24. A batsman scores 87 runs in the 17th inning and increases his average by 3. Find his average after 17th inning.", "Answer: 39\nSolution: Let avg after 16 innings = x. 16x + 87 = 17(x+3). x = 36. New avg = 39."),
        ("25. The average of 10 numbers is 40. If each number is multiplied by 2, what is the new average?", "Answer: 80\nSolution: New average = Old average × 2 = 80."),
    ]),
]

# Add more sections...
more_questions = [
    # Section 6: Profit, Loss & Discount (26-35)
    ("Section 6: Profit, Loss & Discount (26-35)", [
        ("26. A man buys a cycle for Rs. 1400 and sells it at a loss of 15%. Find the selling price.", "Answer: Rs. 1190\nSolution: SP = 1400 × 0.85 = 1190."),
        ("27. If the CP of 12 pens is equal to the SP of 10 pens, find the profit %.", "Answer: 20%\nSolution: 12CP = 10SP → SP/CP = 12/10 = 1.2. Profit = 20%."),
        ("28. A shopkeeper marks his goods 20% above CP and gives a discount of 10%. Find profit %.", "Answer: 8%\nSolution: Let CP=100. MP=120. Discount 10% on 120 = 12. SP=108. Profit = 8%."),
        ("29. By selling 45 lemons for Rs. 40, a man loses 20%. How many should he sell for Rs. 24 to gain 20%?", "Answer: 18\nSolution: SP of 45 = 40. Loss 20% → CP = 40/0.8 = 50. CP per lemon = 50/45 = 10/9. Target SP for 20% gain = 1.2 × CP. No. of lemons = 24 / (1.2 × 10/9) = 18."),
        ("30. Two items are sold at Rs. 990 each. One at 10% profit, other at 10% loss. Find overall %.", "Answer: 1% Loss\nSolution: When SP is same and % profit/loss is same, always loss. Loss % = (x/10)² = (10/10)² = 1%."),
        ("31. A trader mixes 26 kg rice at Rs. 20/kg with 30 kg rice at Rs. 36/kg and sells at Rs. 30/kg. Find profit %.", "Answer: 5%\nSolution: Total CP = 26×20 + 30×36 = 1600. Total Weight = 56 kg. Total SP = 56×30 = 1680. Profit = 80. % = (80/1600)×100 = 5%."),
        ("32. Successive discounts of 10% and 20% are equivalent to a single discount of?", "Answer: 28%\nSolution: 10 + 20 - (10×20)/100 = 30 - 2 = 28%."),
        ("33. If CP is 96% of SP, what is the profit %?", "Answer: 4.16% (approx)\nSolution: Let SP=100, CP=96. Profit=4. % = (4/96)×100 = 4.16%."),
        ("34. A man sells an article at 5% profit. If he had bought it at 5% less and sold it for Re. 1 less, he would have gained 10%. Find CP.", "Answer: Rs. 200\nSolution: Let CP=100. SP=105. New CP=95. New SP for 10% gain = 95×1.1 = 104.5. Diff in SP = 0.5. If diff is 0.5, CP=100. If diff is 1, CP=200."),
        ("35. Marked Price is Rs. 800. Discount 15%. Find SP.", "Answer: Rs. 680\nSolution: 800 × 0.85 = 680."),
    ]),
    
    # Section 7: Simple & Compound Interest (36-40)
    ("Section 7: Simple & Compound Interest (36-40)", [
        ("36. Find SI on Rs. 5000 at 10% for 3 years.", "Answer: Rs. 1500\nSolution: (5000 × 10 × 3)/100 = 1500."),
        ("37. A sum doubles itself in 10 years at SI. Find rate.", "Answer: 10%\nSolution: Interest = Principal. P = (P × R × 10)/100 → R = 10%."),
        ("38. Find CI on Rs. 1000 at 10% for 2 years.", "Answer: Rs. 210\nSolution: 1000(1.1)² - 1000 = 1210 - 1000 = 210."),
        ("39. The difference between CI and SI on a sum for 2 years at 10% is Rs. 50. Find the sum.", "Answer: Rs. 5000\nSolution: Diff = P(R/100)². 50 = P(0.1)² = P(0.01) → P = 5000."),
        ("40. In how many years will a sum become 8 times itself at CI if it doubles in 3 years?", "Answer: 9 years\nSolution: 2³ = 8. So 3 × 3 = 9 years."),
    ]),
    
    # Section 8: Time, Speed & Distance (41-50)
    ("Section 8: Time, Speed & Distance (41-50)", [
        ("41. A car travels 60 km/hr for 2 hours and 40 km/hr for 3 hours. Find average speed.", "Answer: 48 km/hr\nSolution: Total Dist = 120 + 120 = 240. Total Time = 5. Avg Speed = 240/5 = 48."),
        ("42. A train 100m long crosses a pole in 10 seconds. Find speed in km/hr.", "Answer: 36 km/hr\nSolution: Speed = 100/10 = 10 m/s. 10 × 18/5 = 36 km/hr."),
        ("43. Two trains move in opposite directions at 60 km/hr and 40 km/hr. Lengths 140m and 160m. Time to cross?", "Answer: 10.8 seconds\nSolution: Rel Speed = 100 km/hr = 250/9 m/s. Dist = 300m. Time = 300/(250/9) = 10.8 sec."),
        ("44. A man goes to office at 3 km/hr and returns at 2 km/hr. Total time 5 hours. Find distance.", "Answer: 6 km\nSolution: d/3 + d/2 = 5 → 5d/6 = 5 → d = 6."),
        ("45. A boat goes 11 km/hr along stream and 5 km/hr against stream. Speed of boat in still water?", "Answer: 8 km/hr\nSolution: (11+5)/2 = 8."),
        ("46. Speed of boat in still water is 10 km/hr, stream is 2 km/hr. Time to go 48 km downstream?", "Answer: 4 hours\nSolution: Down speed = 12. Time = 48/12 = 4."),
        ("47. A train 150m long runs at 90 km/hr. Time to cross a bridge 200m long?", "Answer: 14 seconds\nSolution: Dist = 350m. Speed = 90×5/18 = 25 m/s. Time = 350/25 = 14."),
        ("48. Walking at 4/5 of usual speed, a man is 10 min late. Find usual time.", "Answer: 40 min\nSolution: Speed ratio 5:4, Time ratio 4:5. 1 unit diff = 10 min. Usual time (4 units) = 40 min."),
        ("49. A covers 100m, B covers 90m in same time. In a 100m race, A beats B by?", "Answer: 10m\nSolution: When A finishes 100, B is at 90. Gap = 10m."),
        ("50. Distance between A and B is 330 km. Train starts from A at 60 km/hr at 8 AM. Another from B at 75 km/hr at 9 AM. When do they meet?", "Answer: 11 AM\nSolution: By 9 AM, A covers 60 km. Dist left = 270. Rel speed = 135. Time = 270/135 = 2 hours. 9 AM + 2 = 11 AM."),
    ]),
]

# Section 9: Time & Work / Pipes (51-60)
more_questions.append(("Section 9: Time & Work / Pipes (51-60)", [
    ("51. A can do work in 10 days, B in 15 days. Together?", "Answer: 6 days\nSolution: LCM(10,15)=30 units. A=3, B=2. Together=5. Days = 30/5 = 6."),
    ("52. A and B together do work in 12 days. A alone in 20 days. B alone?", "Answer: 30 days\nSolution: 1/12 - 1/20 = (5-3)/60 = 2/60 = 1/30."),
    ("53. 10 men can do work in 15 days. How many days for 25 men?", "Answer: 6 days\nSolution: M1D1 = M2D2 → 10×15 = 25×D2 → D2 = 6."),
    ("54. A is twice as good as B. Together they finish in 18 days. A alone?", "Answer: 27 days\nSolution: Ratio eff A:B = 2:1. Total eff = 3. Total work = 3×18 = 54. A alone = 54/2 = 27."),
    ("55. 3 men or 4 women can do work in 43 days. 7 men and 5 women?", "Answer: 12 days\nSolution: 3M = 4W → 1M = 4/3 W. 7M + 5W = 43/3 W. 4W take 43 days. 43/3 W takes (43×4)/(43/3) = 12 days."),
    ("56. Pipe A fills in 10 hrs, Pipe B empties in 15 hrs. Both open?", "Answer: 30 hrs\nSolution: 1/10 - 1/15 = 1/30."),
    ("57. A and B do work for Rs. 600. A takes 6 days, B takes 8 days. With C they finish in 3 days. Share of C?", "Answer: Rs. 75\nSolution: Work done by C in 3 days = 1 - (3/6 + 3/8) = 1/8. Share = 1/8 × 600 = 75."),
    ("58. 12 men work 8 hrs/day for 10 days. How many men to work 12 hrs/day for 5 days?", "Answer: 16 men\nSolution: 12×8×10 = M2×12×5 → 960 = 60M2 → M2 = 16."),
    ("59. A takes 5 hrs more than B. Together 6 hrs. B alone?", "Answer: 10 hours\nSolution: 1/x + 1/(x+5) = 1/6. Solve: x² - 7x - 30 = 0 → x = 10."),
    ("60. A tank is 1/5 full. 22 liters added to make it 3/4 full. Capacity?", "Answer: 40 liters\nSolution: 3/4 - 1/5 = 11/20. 11/20 of Cap = 22. Cap = 22×20/11 = 40."),
]))

# Section 10: Permutation & Combination (61-65)
more_questions.append(("Section 10: Permutation & Combination (61-65)", [
    ("61. How many ways to arrange letters of 'APPLE'?", "Answer: 60\nSolution: Total 5, P repeats 2. 5!/2! = 120/2 = 60."),
    ("62. In how many ways can a committee of 3 be formed from 5 men and 3 women with at least 1 woman?", "Answer: 46\nSolution: Total ways 8C3 = 56. No woman (all men) 5C3 = 10. At least 1 = 56 - 10 = 46."),
    ("63. How many 3-digit numbers can be formed from 1,2,3,4,5 without repetition?", "Answer: 60\nSolution: 5×4×3 = 60."),
    ("64. How many ways to select 5 players from 10?", "Answer: 252\nSolution: 10C5 = 252."),
    ("65. Vowels together in 'LEADER'?", "Answer: 72\nSolution: Vowels E,A,E (3). Consonants L,D,R (3). Treat vowels as 1 unit. Total 4 units. 4! × (3!/2!) = 24 × 3 = 72."),
]))

# Section 11: Probability (66-70)
more_questions.append(("Section 11: Probability (66-70)", [
    ("66. Probability of getting a head in a single coin toss?", "Answer: 1/2\nSolution: 1 favorable, 2 total."),
    ("67. Probability of getting a sum of 9 when two dice are thrown?", "Answer: 1/9\nSolution: Pairs (3,6), (4,5), (5,4), (6,3). 4 outcomes. Total 36. 4/36 = 1/9."),
    ("68. A bag has 3 red, 4 green balls. Prob of drawing 2 green?", "Answer: 2/7\nSolution: 4C2 / 7C2 = 6 / 21 = 2/7."),
    ("69. Probability that a leap year has 53 Sundays?", "Answer: 2/7\nSolution: 366 days = 52 weeks + 2 days. 2 days can be (S,M), (M,T)... (S,S). 7 cases. 2 cases have Sunday."),
    ("70. Prob of drawing a king from a deck of cards?", "Answer: 1/13\nSolution: 4 Kings, 52 cards. 4/52 = 1/13."),
]))

# Section 12: Mixtures & Alligation (71-75)
more_questions.append(("Section 12: Mixtures & Alligation (71-75)", [
    ("71. In what ratio must tea at Rs. 60/kg be mixed with tea at Rs. 90/kg to get Rs. 70/kg?", "Answer: 2:1\nSolution: Alligation: (90-70) : (70-60) = 20:10 = 2:1."),
    ("72. A vessel has 40L milk. 4L removed and replaced with water. Repeated 3 times. Milk left?", "Answer: 29.16 L\nSolution: 40 × (1 - 4/40)³ = 40 × (0.9)³ = 40 × 0.729 = 29.16."),
    ("73. Ratio of water to milk to gain 20% by selling at CP?", "Answer: 1:5\nSolution: CP of mixture = SP/1.2. Let SP=1. CP=5/6. Milk cost 1, Water 0. Ratio (5/6 - 0) : (1 - 5/6) = 5:1 (Milk:Water). Water:Milk = 1:5."),
    ("74. 20L mixture has 10% water. How much water to add to make 20% water?", "Answer: 2.5 L\nSolution: Water = 2L, Milk = 18L. New mix: Milk is 80%. Total = 18/0.8 = 22.5. Water added = 22.5 - 20 = 2.5."),
    ("75. Zinc and Copper ratio 5:3 in 400g alloy. How much copper to add to make ratio 5:4?", "Answer: 50g\nSolution: Zn=250, Cu=150. New Cu = x. 250/(150+x) = 5/4 → 1000 = 750 + 5x → x = 50."),
]))

# Section 13: Algebra (76-80)
more_questions.append(("Section 13: Algebra (76-80)", [
    ("76. If x + 1/x = 5, find x² + 1/x².", "Answer: 23\nSolution: Square both sides: x² + 1/x² + 2 = 25 → x² + 1/x² = 23."),
    ("77. Solve for x: 2x + 3 = 7.", "Answer: 2\nSolution: 2x = 4 → x = 2."),
    ("78. If a+b=10, ab=21, find a²+b².", "Answer: 58\nSolution: (a+b)² - 2ab = 100 - 42 = 58."),
    ("79. Roots of x² - 5x + 6 = 0.", "Answer: 2, 3\nSolution: (x-2)(x-3)=0."),
    ("80. If x² + y² = 25 and xy = 12, find x+y.", "Answer: 7\nSolution: (x+y)² = 25 + 24 = 49 → x+y = 7."),
]))

# Section 14: Geometry & Mensuration (81-90)
more_questions.append(("Section 14: Geometry & Mensuration (81-90)", [
    ("81. Area of rectangle with length 10, breadth 5.", "Answer: 50 sq units\nSolution: L × B = 50."),
    ("82. Circumference of circle radius 7 cm.", "Answer: 44 cm\nSolution: 2πr = 2 × 22/7 × 7 = 44."),
    ("83. Volume of cube side 4 cm.", "Answer: 64 cm³\nSolution: a³ = 4³ = 64."),
    ("84. Area of triangle base 10, height 8.", "Answer: 40 sq units\nSolution: 1/2 × b × h = 40."),
    ("85. Diagonal of square side 10.", "Answer: 10√2\nSolution: a√2."),
    ("86. Curved surface area of cylinder r=7, h=10.", "Answer: 440 sq units\nSolution: 2πrh = 2 × 22/7 × 7 × 10 = 440."),
    ("87. Volume of cone r=3, h=4.", "Answer: 12π\nSolution: 1/3 πr²h = 1/3 π(9)(4) = 12π."),
    ("88. Surface area of sphere r=3.", "Answer: 36π\nSolution: 4πr² = 4π(9) = 36π."),
    ("89. Perimeter of equilateral triangle side 6.", "Answer: 18\nSolution: 3 × 6 = 18."),
    ("90. If radius of circle increases by 10%, area increases by?", "Answer: 21%\nSolution: (1.1)² = 1.21 → 21%."),
]))

# Section 15: Statistics (91-95)
more_questions.append(("Section 15: Statistics (91-95)", [
    ("91. Mean of 2, 4, 6, 8, 10.", "Answer: 6\nSolution: Sum=30, Count=5. Mean=6."),
    ("92. Median of 1, 3, 5, 7, 9.", "Answer: 5\nSolution: Middle value is 5."),
    ("93. Mode of 2, 3, 3, 4, 5.", "Answer: 3\nSolution: Most frequent is 3."),
    ("94. Range of 10, 20, 30, 40.", "Answer: 30\nSolution: Max - Min = 40 - 10 = 30."),
    ("95. If mean of 5 numbers is 10, sum is?", "Answer: 50\nSolution: 5 × 10 = 50."),
]))

# Section 16: Data Interpretation (96-100)
more_questions.append(("Section 16: Data Interpretation (96-100)\n*Data: Sales of Company A (in Lakhs): 2020: 10, 2021: 15, 2022: 20, 2023: 25, 2024: 30.*", [
    ("96. What is the average sales from 2020 to 2024?", "Answer: 20 Lakhs\nSolution: (10+15+20+25+30)/5 = 100/5 = 20."),
    ("97. What is the % increase from 2020 to 2021?", "Answer: 50%\nSolution: (15-10)/10 × 100 = 50%."),
    ("98. In which year was the increase maximum?", "Answer: All equal (5 Lakhs each year)\nSolution: Increase is constant 5 Lakhs."),
    ("99. Total sales in 2023 and 2024?", "Answer: 55 Lakhs\nSolution: 25 + 30 = 55."),
    ("100. If 2025 sales increase by 20% over 2024, find 2025 sales.", "Answer: 36 Lakhs\nSolution: 30 × 1.2 = 36."),
]))

# Combine all questions
all_sections = questions + more_questions

# Generate PDF content
for section_title, section_questions in all_sections:
    pdf.chapter_title(section_title)
    for q, a in section_questions:
        pdf.set_font('Arial', 'B', 9)
        pdf.multi_cell(0, 5, q)
        pdf.set_font('Arial', '', 9)
        pdf.multi_cell(0, 5, a)
        pdf.ln(2)
    pdf.ln(5)

# Save PDF
filename = "TCS_NQT_100_Aptitude_Problems.pdf"
pdf.output(filename)
print(f"PDF created successfully: {filename}")
 # Result execute error ```