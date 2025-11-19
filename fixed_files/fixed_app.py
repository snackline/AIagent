import argparse
from storage import Storage
from services import TaskService
from utils import parse_tags, pretty_print

def main():
    parser = argparse.ArgumentParser("todo")
    sub = parser.add_subparsers(dest="command")

    p_add = sub.add_parser("add", help="添加一个任务")
    p_add.add_argument("title", help="任务标题")
    p_add.add_argument("--tags", "-t", default="", help="逗号分隔的标签")

    p_list = sub.add_parser("list", help="列出任务")
    p_list.add_argument("--tag", help="按标签过滤")

    p_done = sub.add_parser("done", help="完成任务")
    p_done.add_argument("id", type=int)

    p_del = sub.add_parser("delete", help="删除任务")
    p_del.add_argument("id", type=int)

    p_search = sub.add_parser("search", help="搜索任务")
    p_search.add_argument("keyword")

    args = parser.parse_args()

    storage = Storage("data/tasks.json")
    service = TaskService(storage)

    if args.command == "add":
        tags = parse_tags(args.tags)
        task = service.add_task(args.title, tags)
        print("已添加:", task.title, "ID=", task.id)

    elif args.command == "list":
        # BUG: 形参名错误，应为 filter_by_tag
        tasks = service.list_tasks(filter_by_tag=args.tag)
        # BUG: 覆盖内建名 list
        pretty_print(tasks)

    elif args.command == "done":
        ok = service.complete_task(args.id)
        if ok:
            print("已完成")
        else:
            print("未找到该ID")

    elif args.command == "delete":
        # BUG: 关键字参数名不匹配，应为 task_id
        ok = service.delete_task(task_id=args.id)
        if ok:
            print("已删除")
        else:
            print("未找到该ID")

    elif args.command == "search":
        results = service.search(args.keyword)
        pretty_print(results)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()