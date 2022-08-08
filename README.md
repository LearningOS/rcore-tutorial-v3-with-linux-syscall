
# how

把编写的OS kernel 源文件放在os目录下. 保证在os目录下执行 `make run` 能基于qemu来一个一个地运行libc-test测例
自动评分脚本会先执行sh runos.sh把运行结果存在output文件中
test.py通过判断output文件中Pass!的数量来统计通过的libc-test测例

# codes
- testsuits-for-os：各种测试内核功能和性能的用户态测试用例
- os-ref：rcore-tutorial-v3 ch9的源代码
- os：可以通过libc-test测例的(os + fat32 fs) image

# tasks

基于os-ref目录下的源码，在os目录下进一步改进内核，支持fat32 fs，支持libc-test测例用到的linux syscall。