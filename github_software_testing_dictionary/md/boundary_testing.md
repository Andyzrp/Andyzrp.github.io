# 边界测试

边界值分析是一种黑盒子或基于规范的测试技术，其中使用边界值执行测试。

## 例

考试的通过边界为 50%，良为 75%，优为 85%。此方案的有效边界值如下：

```vi
49, 50 - 通过
74, 75 - 良
84, 85 - 优
```

边界值针对有效边界和无效边界进行验证。

上例中的无效边界情况可以如下给出：

```vi
0 - 对于下限边值
101 - 对于上限边值
```