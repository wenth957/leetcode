library("quantmod")
library("tidyquant")
library("rugarch")
library("copula")
library("VGAM")
library("ggplot2")
library("GoFKernel")
library("mistr")
library("tseries")
library("stats")
library("fDMA")
library("xts")
# 设置工作空间
setwd("D:/paper")
getwd()
# 第一部分：实证设计
# 2.1 导入数据和描述性统计
nobank <- read.csv("./nobank.csv", sep = ",", header = T)
bank <- read.csv("./bank.csv", sep = ",", header = T)
house <- read.csv("./house.csv", sep = ",", header = T)
data <- read.csv("./data.csv", sep = ",", header = T)
return1 <- as.numeric(sub("%", "", nobank$rnbank))
return2 <- as.numeric(sub("%", "", bank$rbank))
return3 <- as.numeric(sub("%", "", house$rhouse))
return4 <- as.numeric(sub("%", "", data$rdata))
rbind(summary(return1), summary(return2), summary(return3), summary(return4))
# 2.2 数据清洗
## 2.2.1 缩尾处理
contract <- function(df) {
    names(df) <- c("date", "return")
    return <- as.numeric(sub("%", "", df$return))
    df$return <- return
    q1 <- quantile(df$return, 0.01) # 取得时1%时的变量值
    q99 <- quantile(df$return, 0.99) # 取得时99%时的变量值
    df[df$return < q1, ]$return <- q1
    df[df$return > q99, ]$return <- q99
    df
}
nobank <- contract(nobank)
bank <- contract(bank)
house <- contract(house)
data <- contract(data)
rbind(summary(nobank$return), summary(bank$return), summary(house$return), summary(data$return))

cleandata <- function(df) {
    names(df) <- c("date", "return")
    date <- ymd(as.character(df$date))
    df <- xts(df$return, order.by = date)
    df
}
nobank <- cleandata(nobank)
bank <- cleandata(bank)
house <- cleandata(house)
data <- cleandata(data)
## 2.2.2 时序图
layout(matrix(c(1, 2, 3, 4), 2, 2, byrow = TRUE))
plot(nobank, col = "darkorange2", lwd = 1.5)
plot(bank, col = "deeppink3", lwd = 1.5)
plot(house, col = "red", lwd = 1.5)
plot(data, col = "blue", lwd = 1.5)
layout(matrix(c(1), 1, 1))
plot(cbind(nobank, bank, house, data), col = c("darkorange2", "deeppink3", "red", "blue"), lwd = 1.5)

# 2.3 ARCH效应检验
# 2.3.1 LJUNG BOX TEST  H0:无自相关
LJtest_nobank_return <- Box.test(nobank)
LJtest_bank_return <- Box.test(bank)
LJtest_house_return <- Box.test(house)
LJtest_data_return <- Box.test(data)

LJtest_return <- matrix(c(LJtest_nobank_return$statistic, LJtest_nobank_return$p.value, LJtest_bank_return$statistic, LJtest_bank_return$p.value, LJtest_house_return$statistic, LJtest_house_return$p.value, LJtest_data_return$statistic, LJtest_data_return$p.value), 2, 4)
dimnames(LJtest_return) <- list(c("LJung-Box TS", "LJung-Box p-value"), c("nobank", "bank", "house", "data"))
LJtest_return
# 2.3.2 arch检验
# ENGLE'S ARCH TEST LM检验，滞后项是否存在自相关
ARCHtest_nobank_return <- archtest(as.vector(nobank))
ARCHtest_bank_return <- archtest(as.vector(bank))
ARCHtest_house_return <- archtest(as.vector(house))
ARCHtest_data_return <- archtest(as.vector(data))

ARCHtest_return <- matrix(c(ARCHtest_nobank_return$statistic, ARCHtest_nobank_return$p.value, ARCHtest_bank_return$statistic, ARCHtest_bank_return$p.value, ARCHtest_house_return$statistic, ARCHtest_house_return$p.value, ARCHtest_data_return$statistic, ARCHtest_data_return$p.value), 2, 4)
dimnames(ARCHtest_return) <- list(c("Engle-ARCH TS", "Engle-ARCH p-value"), c("nobank", "bank", "house", "data"))
ARCHtest_return
# 2.4 ARMA定阶
order_EACF <- function(p_max, q_max, data) {
    final.aic <- Inf
    final.order <- c(0, 0, 0)
    for (p in 0:p_max) {
        for (q in 0:q_max) {
            if (p == 0 && q == 0) {
                next
            }
            arimaFit <- tryCatch(arima(data, order = c(p, 0, q)),
                error = function(err) FALSE,
                warning = function(err) FALSE
            )
            if (!is.logical(arimaFit)) {
                current.aic <- AIC(arimaFit)
                if (current.aic < final.aic) {
                    final.aic <- current.aic
                    final.order <- c(p, 0, q)
                    final.arima <- arima(data, order = final.order)
                }
            }
            else {
                next
            }
        }
    }
    return(c(final.order, final.aic))
}
order_nobank <- order_EACF(4, 4, nobank)
order_bank <- order_EACF(4, 4, bank)
order_house <- order_EACF(4, 4, house)
order_data <- order_EACF(4, 4, data)
rbind(order_nobank, order_bank, order_house, order_data)
# 2.5 新息分布的确定
# 收益率正态性检验JB检验和qq图
# 2.5.1 jb检验 H0:服从正态分布
# Jarque-Bera test for log-return
JBtest_nobank_return <- jarque.bera.test(nobank)
JBtest_bank_return <- jarque.bera.test(bank)
JBtest_house_return <- jarque.bera.test(house)
JBtest_data_return <- jarque.bera.test(data)

JBtest_return <- matrix(c(JBtest_nobank_return$statistic, JBtest_nobank_return$p.value, JBtest_bank_return$statistic, JBtest_bank_return$p.value, JBtest_house_return$statistic, JBtest_house_return$p.value, JBtest_data_return$statistic, JBtest_data_return$p.value), 2, 4)
dimnames(JBtest_return) <- list(c("Jarque-Bera TS", "Jarque-Bera p-value"), c("nobank", "bank", "house", "data"))
JBtest_return
# 2.5.2 qq图
layout(matrix(c(1, 2, 3, 4), 2, 2, byrow = TRUE))
qqnorm(nobank, main = "nobank log return")
qqline(nobank, col = "darkorange2")

qqnorm(bank, main = "bank log return")
qqline(bank, col = "deeppink3")

qqnorm(house, main = "house log return")
qqline(house, col = "red")

qqnorm(data, main = "data log return")
qqline(data, col = "blue")
# 2.5.3 自相关函数、偏自相关函数
layout(matrix(c(1, 2, 3, 4), 2, 2, byrow = TRUE))
acf(nobank, main = "nobank ACF")
acf(bank, main = "bank ACF")
acf(house, main = "house ACF")
acf(data, main = "data ACF")
layout(matrix(c(1, 2, 3, 4), 2, 2, byrow = TRUE))
pacf(nobank, main = "nobank PACF")
pacf(bank, main = "bank PACF")
pacf(house, main = "house PACF")
pacf(data, main = "data PACF")
# 第二部分：结果分析
# 拟合ARMA-Garch模型得到标准化残差
garchspec_nobank <- ugarchspec(
    mean.model = list(armaOrder = c(order_nobank[1], order_nobank[3])),
    variance.model = list(model = "gjrGARCH", garchOrder = c(1, 1)),
    distribution.model = "sstd"
)
garchfit_nobank <- ugarchfit(data = nobank, spec = garchspec_nobank)
coef(garchfit_nobank)
# 标准化残差
standardize_residual_nobank <- residuals(garchfit_nobank) / sigma(garchfit_nobank)
# PloTing
layout(matrix(c(1, 2, 3, 4), 2, 2, byrow = TRUE))
acf(standardize_residual_nobank, main = "nobank residual ACF")
pacf(standardize_residual_nobank, main = "nobank residual PACF")
plot(standardize_residual_nobank, main = "residual", col = "darkorange2", lwd = 1)
qqnorm(standardize_residual_nobank, main = "nobank qq-plot")
qqline(standardize_residual_nobank, col = "darkorange2")
# 银行
garchspec_bank <- ugarchspec(
    mean.model = list(armaOrder = c(order_bank[1], order_bank[3])),
    variance.model = list(model = "gjrGARCH", garchOrder = c(1, 1)),
    distribution.model = "sstd"
)
garchfit_bank <- ugarchfit(data = bank, spec = garchspec_bank)
coef(garchfit_bank)
# 标准化残差
standardize_residual_bank <- residuals(garchfit_bank) / sigma(garchfit_bank)
# Plotting
layout(matrix(c(1, 2, 3, 4), 2, 2, byrow = TRUE))
acf(standardize_residual_bank, main = "bank residual ACF")
pacf(standardize_residual_bank, main = "bank residual PACF")
plot(standardize_residual_bank, main = "residual", col = "darkorange2", lwd = 1)
qqnorm(standardize_residual_bank, main = "bank qq-plot")
qqline(standardize_residual_bank, col = "darkorange2")

# 地产
garchspec_house <- ugarchspec(
    mean.model = list(armaOrder = c(order_house[1], order_house[3])),
    variance.model = list(model = "gjrGARCH", garchOrder = c(1, 1)),
    distribution.model = "sstd"
)
garchfit_house <- ugarchfit(data = house, spec = garchspec_house)
coef(garchfit_house)
# 标准化残差
standardize_residual_house <- residuals(garchfit_house) / sigma(garchfit_house)
# Plotting
layout(matrix(c(1, 2, 3, 4), 2, 2, byrow = TRUE))
acf(standardize_residual_house, main = "house residual ACF")
pacf(standardize_residual_house, main = "house residual PACF")
plot(standardize_residual_house, main = "residual", col = "darkorange2", lwd = 1)
qqnorm(standardize_residual_house, main = "house qq-plot")
qqline(standardize_residual_house, col = "darkorange2")
# 大数据
garchspec_data <- ugarchspec(
    mean.model = list(armaOrder = c(order_data[1], order_data[3])),
    variance.model = list(model = "gjrGARCH", garchOrder = c(1, 1)),
    distribution.model = "sstd"
)
garchfit_data <- ugarchfit(data = data, spec = garchspec_data)
coef(garchfit_data)
# 标准化残差
standardize_residual_data <- residuals(garchfit_data) / sigma(garchfit_data)
# Plotting
layout(matrix(c(1, 2, 3, 4), 2, 2, byrow = TRUE))
acf(standardize_residual_data, main = "data residual ACF")
pacf(standardize_residual_data, main = "data residual PACF")
plot(standardize_residual_data, main = "residual", col = "darkorange2", lwd = 1)
qqnorm(standardize_residual_data, main = "data qq-plot")
qqline(standardize_residual_data, col = "darkorange2")
# 直方图
# Histogram of each standardized residuals
layout(matrix(c(1, 2, 3, 4), 2, 2, byrow = TRUE))
hist(standardize_residual_nobank, main = "nobank standardized residual", breaks = 70, col = "darkorange2")
hist(standardize_residual_bank, main = "bank standardized residual", breaks = 70, col = "deeppink3")
hist(standardize_residual_house, main = "house standardized residual", breaks = 70, col = "red")
hist(standardize_residual_data, main = "data standardized residual", breaks = 70, col = "blue")


# 残差混成检验
LJtest_nobank_residual <- Box.test(standardize_residual_nobank)
LJtest_bank_residual <- Box.test(standardize_residual_bank)
LJtest_house_residual <- Box.test(standardize_residual_house)
LJtest_data_residual <- Box.test(standardize_residual_data)

LJtest_residual <- matrix(c(LJtest_nobank_residual$statistic, LJtest_nobank_residual$p.value, LJtest_bank_residual$statistic, LJtest_bank_residual$p.value, LJtest_house_residual$statistic, LJtest_house_residual$p.value, LJtest_data_residual$statistic, LJtest_data_residual$p.value), 2, 4)
dimnames(LJtest_residual) <- list(c("LJung-Box TS", "LJung-Box p-value"), c("nobank", "bank", "house", "data"))
LJtest_residual

# 回报率存在ARCH效应
ARCHtest_nobank_residual <- archtest(as.vector(standardize_residual_nobank))
ARCHtest_bank_residual <- archtest(as.vector(standardize_residual_bank))
ARCHtest_house_residual <- archtest(as.vector(standardize_residual_house))
ARCHtest_data_residual <- archtest(as.vector(standardize_residual_data))
# 残差ARCH检验
ARCHtest_residual <- matrix(c(ARCHtest_nobank_residual$statistic, ARCHtest_nobank_residual$p.value, ARCHtest_bank_residual$statistic, ARCHtest_bank_residual$p.value, ARCHtest_house_residual$statistic, ARCHtest_house_residual$p.value, ARCHtest_data_residual$statistic, ARCHtest_data_residual$p.value), 2, 4)
dimnames(ARCHtest_residual) <- list(c("Engle-ARCH TS", "Engle-ARCH p-value"), c("nobank", "bank", "house", "data"))
ARCHtest_residual
# 残差不存在arch效应
summary_testing <- rbind(rep(1, 4), rep(0, 4), c(0, 0, 0, 0), rep(1, 4), rep(0, 4))
dimnames(summary_testing) <- list(c("Jarque-Bera test", "LJung-Box test (return)", "LJung-Box test (residual)", "Engle-ARCH test (return)", "Engle-ARCH test (residual)"), c("nobank", "bank", "house", "data"))
summary_testing
# 序列化残差
x_nobank <- coredata(standardize_residual_nobank)
x_bank <- coredata(standardize_residual_bank)
x_house <- coredata(standardize_residual_house)
x_data <- coredata(standardize_residual_data)
fit_nobank <- GNG_fit(standardize_residual_nobank, start = c(break1 = -2, break2 = 1.5, mean = 0, sd = 1, shape1 = 0.1, shape2 = 0.1))
fit_nobank
fit_bank <- GNG_fit(standardize_residual_bank, start = c(break1 = -2, break2 = 1.5, mean = 0, sd = 1, shape1 = 0.1, shape2 = 0.1))
fit_bank
fit_house <- GNG_fit(standardize_residual_house, start = c(break1 = -2, break2 = 1.5, mean = 0, sd = 1, shape1 = 0.1, shape2 = 0.1))
fit_data <- GNG_fit(standardize_residual_data, start = c(break1 = -2, break2 = 1.5, mean = 0, sd = 1, shape1 = 0.1, shape2 = 0.1))
plot(fit_nobank)
plot(fit_bank)
plot(fit_house)
plot(fit_data)
# cdf
layout(matrix(c(1, 2, 3, 4), 2, 2, byrow = TRUE))
plot(fit_nobank, which = "cdf", main1 = "nobank residual cdf")
plot(fit_bank, which = "cdf", main1 = "bank residual cdf")
plot(fit_house, which = "cdf", main1 = "house residual cdf")
plot(fit_data, which = "cdf", main1 = "data residual cdf")

# 计算PDF CDF 和逆 CDF
# nobank
PDF_nobank <- function(x) {
    d(distribution(fit_nobank), x)
}
CDF_nobank <- function(x) {
    p(distribution(fit_nobank), x)
}
inverse_CDF_nobank <- function(x) {
    q(distribution(fit_nobank), x)
}

# bank
PDF_bank <- function(x) {
    d(distribution(fit_bank), x)
}
CDF_bank <- function(x) {
    p(distribution(fit_bank), x)
}
inverse_CDF_bank <- function(x) {
    q(distribution(fit_bank), x)
}

# house
PDF_house <- function(x) {
    d(distribution(fit_house), x)
}
CDF_house <- function(x) {
    p(distribution(fit_house), x)
}
inverse_CDF_house <- function(x) {
    q(distribution(fit_house), x)
}

# data
PDF_data <- function(x) {
    d(distribution(fit_data), x)
}
CDF_data <- function(x) {
    p(distribution(fit_data), x)
}
inverse_CDF_data <- function(x) {
    q(distribution(fit_data), x)
}
# graph
# pdf图
layout(matrix(c(1, 2, 3, 4), 2, 2, byrow = TRUE))
curve(PDF_nobank, -3, 3, col = "darkorange2")
curve(PDF_bank, -3, 3, col = "deeppink3")
curve(PDF_house, -3, 3, col = "red")
curve(PDF_data, -3, 3, col = "blue")
# cdf图
layout(matrix(c(1, 2, 3, 4), 2, 2, byrow = TRUE))
curve(CDF_nobank, -3, 3, col = "darkorange2")
curve(CDF_bank, -3, 3, col = "deeppink3")
curve(CDF_house, -3, 3, col = "red")
curve(CDF_data, -3, 3, col = "blue")
# 逆cdf图
layout(matrix(c(1, 2, 3, 4), 2, 2, byrow = TRUE))
curve(inverse_CDF_nobank, col = "darkorange2")
curve(inverse_CDF_bank, col = "deeppink3")
curve(inverse_CDF_house, col = "red")
curve(inverse_CDF_data, col = "blue")
# 标准化残差转化为均匀分布数据
U_nobank <- CDF_nobank(standardize_residual_nobank)
U_bank <- CDF_bank(standardize_residual_bank)
U_house <- CDF_house(standardize_residual_house)
U_data <- CDF_data(standardize_residual_data)
all_data <- cbind(U_nobank, U_bank, U_house, U_data)
# 残差间相关性分析
layout(matrix(c(1, 2, 3, 4, 5, 6), 3, 2, byrow = TRUE))
plot(x_nobank, x_bank)
plot(x_nobank, x_house)
plot(x_nobank, x_data)
plot(x_bank, x_house)
plot(x_bank, x_data)
plot(x_house, x_data)
# 概率积分变换后相关性缝隙
plot(U_nobank, U_bank)
plot(U_nobank, U_house)
plot(U_nobank, U_data)
plot(U_bank, U_house)
plot(U_bank, U_data)
plot(U_house, U_data)
# 相关性检验
# Spearman's rho
rho <- cor(all_data, method = "spearman")
rho
# Kendall tau
kendall <- cor(all_data, method = "kendall")
kendall
# 求解copula参数
X <- as.matrix(all_data)
fit_Gaussian <- fitCopula(normalCopula(dim = 4, dispstr = "un"), X, method = "ml")
summary(fit_Gaussian)
fit_tStudent <- fitCopula(tCopula(dim = 4, dispstr = "un"), X, method = "ml")
summary(fit_tStudent)
rbind(coef(fit_Gaussian), coef(fit_tStudent)[-7])
# 抽取copula函数
# Gaussian Copula
Gaussian_model <- normalCopula(coef(fit_Gaussian), dim = 4, dispstr = "un")
getSigma(Gaussian_model)
# T copula
T_model <- tCopula(coef(fit_tStudent)[-7], dim = 4, dispstr = "un", df = coef(fit_tStudent)[7])
getSigma(T_model)
# 蒙特卡洛模拟：1000样本，并且转换为对数收益率
n <- 1000
m <- nrow(all_data)
## 生成矩阵
nobank_matrix_G <- matrix(rep(0, n * m), nrow = m)
bank_matrix_G <- matrix(rep(0, n * m), nrow = m)
house_matrix_G <- matrix(rep(0, n * m), nrow = m)
data_matrix_G <- matrix(rep(0, n * m), nrow = m)
nobank_matrix_T <- matrix(rep(0, n * m), nrow = m)
bank_matrix_T <- matrix(rep(0, n * m), nrow = m)
house_matrix_T <- matrix(rep(0, n * m), nrow = m)
data_matrix_T <- matrix(rep(0, n * m), nrow = m)
## 模拟gaussian残差 rcopula生成随机变量取值 m行4列，1000次
for (i in 1:n) {
    set.seed(i)
    U <- rCopula(m, copula = Gaussian_model)
    nobank_matrix_G[, i] <- inverse_CDF_nobank(U[, 1])
    bank_matrix_G[, i] <- inverse_CDF_bank(U[, 2])
    house_matrix_G[, i] <- inverse_CDF_house(U[, 3])
    data_matrix_G[, i] <- inverse_CDF_data(U[, 4])
}
sim_nobank_G <- xts(x = nobank_matrix_G, order.by = index(standardize_residual_nobank))
sim_bank_G <- xts(x = bank_matrix_G, order.by = index(standardize_residual_bank))
sim_house_G <- xts(x = house_matrix_G, order.by = index(standardize_residual_house))
sim_data_G <- xts(x = data_matrix_G, order.by = index(standardize_residual_data))
# Plotting
# layout(matrix(c(1, 2, 1, 2), 2, 2))
# plot(sim_nobank_G, ylim = c(-6, 6), main = "Simulated S.RESIDUAL-nobank (Gaussian)", lwd = 0.5)
# plot(sim_bank_G, ylim = c(-6, 6), main = "Simulated S.RESIDUAL-bank (Gaussian)", lwd = 0.5)
# plot(sim_house_G, ylim = c(-6, 6), main = "Simulated S.RESIDUAL-house (Gaussian)", lwd = 0.5)
# plot(sim_data_G, ylim = c(-6, 6), main = "Simulated S.RESIDUAL-data (Gaussian)", lwd = 0.5)
## 模拟t分布残差  rcopula生成随机变量取值 m行4列，1000次
for (i in 1:n) {
    set.seed(i)
    U <- rCopula(m, copula = T_model)
    nobank_matrix_T[, i] <- inverse_CDF_nobank(U[, 1])
    bank_matrix_T[, i] <- inverse_CDF_bank(U[, 2])
    house_matrix_T[, i] <- inverse_CDF_house(U[, 3])
    data_matrix_T[, i] <- inverse_CDF_data(U[, 4])
}
sim_nobank_T <- xts(x = nobank_matrix_T, order.by = index(standardize_residual_nobank))
sim_bank_T <- xts(x = bank_matrix_T, order.by = index(standardize_residual_bank))
sim_house_T <- xts(x = house_matrix_T, order.by = index(standardize_residual_house))
sim_data_T <- xts(x = data_matrix_T, order.by = index(standardize_residual_data))
# Plot
# layout(matrix(c(1, 2, 1, 2), 2, 2))
# plot(sim_nobank_T, ylim = c(-7, 7), main = "Simulated S.RESIDUAL-nobank (T)", lwd = 0.5)
# plot(sim_bank_T, ylim = c(-7, 7), main = "Simulated S.RESIDUAL-bank (T)", lwd = 0.5)
# plot(sim_house_T, ylim = c(-7, 7), main = "Simulated S.RESIDUAL-house (T)", lwd = 0.5)
# plot(sim_data_T, ylim = c(-7, 7), main = "Simulated S.RESIDUAL-data (T)", lwd = 0.5)
# 将残差利用arma_garch转化为对数收益率
# 模拟log-return
log_return <- function(model, sim, num_col) {
    sigma_matrix <- coredata(sigma(model))
    diagonal_sigma <- diag(as.numeric(sigma_matrix), nrow = length(sigma_matrix))
    simulated_residuals <- diagonal_sigma %*% sim
    # sigma*标准化残差=原始残差
    simulated_log_returns <- simulated_residuals + matrix(rep(as.numeric(coredata(fitted(model))), num_col), ncol = num_col)
    simulated_log_returns <- xts(simulated_log_returns, order.by = index(sigma(model)))
    simulated_log_returns
}

return_nobank_G <- log_return(garchfit_nobank, sim_nobank_G, num_col = n)
return_bank_G <- log_return(garchfit_bank, sim_bank_G, num_col = n)
return_house_G <- log_return(garchfit_house, sim_house_G, num_col = n)
return_data_G <- log_return(garchfit_data, sim_data_G, num_col = n)
# Plotting
# layout(matrix(c(1, 2, 1, 2), 2, 2))
# plot(return_nobank_G, main = "Simulated RETURN-nobank (Gaussian)", lwd = 0.5)
# plot(return_bank_G, main = "Simulated RETURN-bank (Gaussian)", lwd = 0.5)
# plot(return_house_G, main = "Simulated RETURN-house (Gaussian)", lwd = 0.5)
# plot(return_data_G, main = "Simulated RETURN-data (Gaussian)", lwd = 0.5)
# T-copula
return_nobank_T <- log_return(garchfit_nobank, sim_nobank_T, num_col = n)
return_bank_T <- log_return(garchfit_bank, sim_bank_T, num_col = n)
return_house_T <- log_return(garchfit_house, sim_house_T, num_col = n)
return_data_T <- log_return(garchfit_data, sim_data_T, num_col = n)
# Plot
# layout(matrix(c(1, 2, 1, 2), 2, 2))
# plot(return_nobank_T, main = "Simulated RETURN-nobank (T)", lwd = 0.5)
# plot(return_bank_T, main = "Simulated RETURN-bank (T)", lwd = 0.5)
# plot(return_house_T, main = "Simulated RETURN-house (T)", lwd = 0.5)
# plot(return_data_T, main = "Simulated RETURN-data (T)", lwd = 0.5)
# 计算VaR
weight <- c(0.25, 0.25, 0.25, 0.25)
# real_port_return
real_port_return <- (weight[1] * nobank) + (weight[2] * bank) + (weight[3] * house) + (weight[4] * data)
# Plot
# plot(real_port_return, ylim = c(-5, 5), main = "real portfolio return", lwd = 1, col = "darkblue")
# portfolio return
port_return_G <- weight[1] * return_nobank_G + weight[2] * return_bank_G + weight[3] * return_house_G + weight[4] * return_data_G

# VaR 99
VaR99_return_G <- xts(matrix(rep(1, m), ncol = 1), order.by = index((port_return_G)))
for (i in 1:m) {
    VaR99_return_G[i, ] <- quantile(port_return_G[i, ], p = 0.01)
}

# VaR 95
VaR95_return_G <- xts(matrix(rep(1, m), ncol = 1), order.by = index((port_return_G)))
for (i in 1:m) {
    VaR95_return_G[i, ] <- quantile(port_return_G[i, ], p = 0.05)
}

# VaR 90
VaR90_return_G <- xts(matrix(rep(1, m), ncol = 1), order.by = index((port_return_G)))
for (i in 1:m) {
    VaR90_return_G[i, ] <- quantile(port_return_G[i, ], p = 0.1)
}
# Plotting
# layout(matrix(c(1, 2, 1, 2), 2, 2))
# plot(port_return_G, ylim = c(-10, 10), main = "Simulated port_return (Gaussian)", lwd = 0.5)
layout(matrix(c(1, 2, 3), 3, 1))
VaRplot(0.01, real_port_return, VaR99_return_G)
VaRplot(0.05, real_port_return, VaR95_return_G)
VaRplot(0.1, real_port_return, VaR90_return_G)
layout(matrix(c(1), 1, 1))
plot(cbind(real_port_return, VaR99_return_G, VaR95_return_G, VaR90_return_G), col = c("black", "deeppink3", "darkorange2", "blue"), main = "GAUSSIAN COPULA", lwd = 0.7)
# portfolio return
port_return_T <- weight[1] * return_nobank_T + weight[2] * return_bank_T + weight[3] * return_house_T + weight[4] * return_data_T
# VaR 99
VaR99_return_T <- xts(matrix(rep(1, m), ncol = 1), order.by = index((port_return_T)))
for (i in 1:m) {
    VaR99_return_T[i, ] <- quantile(port_return_T[i, ], p = 0.01)
}

# VaR 95
VaR95_return_T <- xts(matrix(rep(1, m), ncol = 1), order.by = index((port_return_T)))
for (i in 1:m) {
    VaR95_return_T[i, ] <- quantile(port_return_T[i, ], p = 0.05)
}

# VaR 90
VaR90_return_T <- xts(matrix(rep(1, m), ncol = 1), order.by = index((port_return_T)))
for (i in 1:m) {
    VaR90_return_T[i, ] <- quantile(port_return_T[i, ], p = 0.1)
}

# Plotting
# layout(matrix(c(1, 2, 1, 2), 2, 2))
# plot(port_return_T, ylim = c(-10, 10), main = "Simulated port_return (T-Student)", lwd = 0.5)
layout(matrix(c(1, 2, 3), 3, 1))
VaRplot(0.01, real_port_return, VaR99_return_T)
VaRplot(0.05, real_port_return, VaR95_return_T)
VaRplot(0.1, real_port_return, VaR90_return_T)
layout(matrix(c(1), 1, 1))
plot(cbind(real_port_return, VaR99_return_T, VaR95_return_T, VaR90_return_T), col = c("black", "deeppink3", "darkorange2", "blue"), main = "T-STUDENT COPULA", lwd = 0.7)
# Gauss与T对比
plot(cbind(real_port_return, VaR99_return_G, VaR99_return_T), col = c("black", "blue", "red"), main = "VAR 99%", lwd = 0.7)
plot(cbind(real_port_return, VaR95_return_G, VaR95_return_T), col = c("black", "blue", "red"), main = "VAR 95%", lwd = 0.7)
plot(cbind(real_port_return, VaR90_return_G, VaR90_return_T), col = c("black", "blue", "red"), main = "VAR 90%", lwd = 0.7)
# 检验
##  5% significance level
# Gaussian Copula
test_99_G <- VaRTest(0.01, real_port_return, VaR99_return_G)
test_95_G <- VaRTest(0.05, real_port_return, VaR95_return_G)
test_90_G <- VaRTest(0.1, real_port_return, VaR90_return_G)

# T Copula
test_99_T <- VaRTest(0.01, real_port_return, VaR99_return_T)
test_95_T <- VaRTest(0.05, real_port_return, VaR95_return_T)
test_90_T <- VaRTest(0.1, real_port_return, VaR90_return_T)
# 两种检验
exceed_G <- c(test_99_G$actual.exceed, test_99_G$expected.exceed, test_95_G$actual.exceed, test_95_G$expected.exceed, test_90_G$actual.exceed, test_90_G$expected.exceed)
Kupiec_G <- c(test_99_G$uc.LRp, test_99_G$uc.Decision, test_95_G$uc.LRp, test_95_G$uc.Decision, test_90_G$uc.LRp, test_90_G$uc.Decision)
Christoffersen_G <- c(test_99_G$cc.LRp, test_99_G$cc.Decision, test_95_G$cc.LRp, test_95_G$cc.Decision, test_90_G$cc.LRp, test_90_G$cc.Decision)
cbind(exceed_G, Kupiec_G, Christoffersen_G)
exceed_T <- c(test_99_T$actual.exceed, test_99_T$expected.exceed, test_95_T$actual.exceed, test_95_T$expected.exceed, test_90_T$actual.exceed, test_90_T$expected.exceed)
Kupiec_T <- c(test_99_T$uc.LRp, test_99_T$uc.Decision, test_95_T$uc.LRp, test_95_T$uc.Decision, test_90_T$uc.LRp, test_90_T$uc.Decision)
Christoffersen_T <- c(test_99_T$cc.LRp, test_99_T$cc.Decision, test_95_T$cc.LRp, test_95_T$cc.Decision, test_90_T$cc.LRp, test_90_T$cc.Decision)
cbind(exceed_T, Kupiec_T, Christoffersen_T)
cbind(Kupiec_G, Christoffersen_G, Kupiec_T, Christoffersen_T)



