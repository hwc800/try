# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hsssssssssssssssssssi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


def handle_git_merge_failure(dddd):
    """
    处理 git merge --strategy-option=theirs MergeAssist 命令执行失败的情况
    """
    import subprocess
    def run_command(cmd):
        """执行命令并返回结果"""
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            return result.returncode, result.stdout, result.stderr
        except Exception as e:
            return -1, "", str(e)

    # 4. 尝试执行合并命令
    print("正在执行合并命令...")
    return_code, stdout, stderr = run_command("git merge --strategy-option=theirs MergeAssist")
    
    if return_code == 0:
        print("合并成功！")
        print(stdout)
        return True
    else:
        print("合并失败！")
        print("错误信息:", stderr)
        
        # 处理合并冲突
        if "CONFLICT" in stderr:
            print("检测到合并冲突，处理方案：")
            print("1. 手动解决冲突后提交")
            print("2. 或者使用其他合并策略")
            print("3. 或者中止合并: git merge --abort")
        
        return False

# 顶顶顶
# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')
    
    # 测试git合并处理函数
    print("\n=== Git合并故障处理测试 ===")
    result = handle_git_merge_failure_eeee()
    print(f"处理结果: {'成功' if result else '失败'}")

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
