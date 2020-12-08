from cosdem import Cosdem

file_name = "example/sample_data.csv"

analyze = Cosdem(file_name)

print(analyze.report())
"""
-- Descriptive Statistics --
               Feature_A  Feature_B
Count             36.000     36.000
Mean              98.250     98.139
Quantile-25       97.000     97.000
Median (Q-50)     99.000     98.000
Quantile-75       99.000     99.000
Std                1.461      1.437
Variance           2.136      2.066
Skewness          -0.520     -0.502
Kurtosis          -0.818     -0.446


-- Homogeneity Tests of Variances --
          Test Statistic  P-value
Levene             0.056    0.814
Bartlett           0.010    0.922


-- Normality Test: Shapiro Wilk --
           Test Statistic  P-value
Feature_A           0.895    0.002
Feature_B           0.917    0.010


-- Statistical Difference Tests --
                Test Statistic  P-value
T-test                   0.325    0.746
Mann Whitney U         615.000    0.354


-- Correlation Tests --
          Test Statistic  P-value
Pearson            0.935      0.0
Spearman           0.940      0.0
Kendall            0.889      0.0


-- Regression Result --
   R Square  Adjusted R Square  P-Value  Coefficient   Bias
0     0.935              0.933      0.0         0.92  7.775
"""