from argparse import ArgumentParser
from Task_controler import Task_controler
# إذا خلصت المشروح وسويت الكوممينتس,سوالبرنت اللي يصير ببداية الأدوات


def main():
    controller = Task_controler('tasks.txt')
    parser = ArgumentParser(description='Simple ClI Task Manager')
    subparser = parser.add_subparsers()

    add_task = subparser.add_parser('add', help="Add the given task")
    add_task.add_argument('title', help="Title pf the task", type=str)
    add_task.add_argument('-d', '--description', help="Short description of the task", type=str, default=None)
    add_task.add_argument('-s', '--start_date', help="Date to begin the task", type=str, default=None)
    add_task.add_argument('-e', '--end_date', help="Date to end the task", type=str, default=None)
    add_task.add_argument('--done', help="Check whether the task is done or not", type=str, default=False)
    add_task.set_defaults(func = controller.add_task)

    list_tasks = subparser.add_parser('list', help='List of unfinished tasks')
    list_tasks.add_argument('-a', '--all', help='List of all the tasks', action='store_true')

    check_task = subparser.add_parser('check', help='Check the given task')
    check_task.add_argument('-t', '--task', help="Number of the task to be done. If not specified, last task will be romved.", type=int)

    remove = subparser.add_parser('remove', help='Remove a task')
    remove.add_argument('-t', '--task', help='The task to be removed (Number)', type=int)

    reset = subparser.add_parser('reset', help='Remove all tasks')


    args = parser.parse_args()
    args.func(args)





if __name__ == '__main__':
    main()