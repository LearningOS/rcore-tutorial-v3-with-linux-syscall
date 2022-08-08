
# how

把编写的OS kernel 源文件放在os目录下. 保证在os目录下执行 `make run` 能基于qemu来一个一个地运行libc-test测例
自动评分脚本会先执行sh runos.sh把运行结果存在output文件中
test.py通过判断output文件中Pass!的数量来统计通过的libc-test测例

# codes
- testsuits-for-os：各种测试内核功能和性能的用户态测试用例，来自[2022全国大学生操作系统比赛内核实现赛道的测例](https://github.com/oscomp/testsuits-for-oskernel/tree/libc-test)
  - libc-test：musl libc的测试套件子集（第一阶段测试用例，是os首先需要通过的测试用例）
  - lua：lua源码（第二阶段测试用例）
  - busybox：busybox源码（第三阶段测试用例）
  - lmbench：lmbench源码（第四阶段测试用例）
- os-ref：rcore-tutorial-v3 ch9的源代码
- os：可以通过libc-test测例的(os + fat32 fs) image

# tasks

- [ ] 基于os-ref目录下的源码，在os目录下进一步改进内核，支持libc-test测例用到的linux syscall
- [ ] 支持fat32 fs
- [ ] 支持lua测例
- [ ] 支持busybox测例
- [ ] 支持lmbench测例