n = int(input("Please enter the number of terms: "))
# n terms in the leibniz series, this is an integer

leibniz_sum = 0 # assigns a value to this variable

for i in range(n):
    leibniz_sum += (-1)**i * (1/(2*i+1))
    # calculates the series given a number of terms

pi = 4 * leibniz_sum # multiplies the series by 4 for an approx. of pi

print("The approximate value of pi is", pi)