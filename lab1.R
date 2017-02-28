x1 = c(1, 2, 3, 4, 5)
y1 = c(1, 2, 1.3, 3.75, 2.25)
x = c(10,
      12,
      13,
      13,
      10,
      10,
      11,
      8,
      8,
      10,
      13,
      10,
      9,
      8,
      10,
      5,
      11,
      10,
      9,
      9,
      10,
      8,
      12,
      11,
      13)

y = c(11,
      13,
      15,
      10,
      12,
      7,
      12,
      10,
      9,
      12,
      13,
      7,
      12,
      6,
      13,
      8,
      12,
      9,
      11,
      11,
      11,
      9,
      9,
      8,
      6)
sx = sum(x)
sy = sum(y)
plot(x, y, type = 'o')
meanx = mean(x)
meany = mean(y)
sumxy = sum(x * y)
sumxx = sum(x * x)
sumyy = sum(y * y)
r = sumxy / sqrt(sumxx * sumyy)
m = r * sy / sx
c = meany - m * meanx

varx = var(x)
vary = var(y)
sdx = sd(x)
sdy = sd(y)



