class TaskSet(object):
    'Basic taskset class'
    cnt = 0

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', type(self).cnt)
        self.task_list = []

        type(self).cnt += 1

    def __del__(self):
        type(self).cnt -= 1

    def __str__(self):
        return "%d\t" % (
            self.id)

    def __len__(self):
        return len(self.task_list)

    def __getitem__(self, idx):
        return self.task_list[idx]

    def __setitem__(self, idx, val):
        self.task_list[idx] = val
        return

    def __iter__(self):
        return iter(self.task_list)

    def append(self, t):
        self.task_list.append(t)
        return

    def clear(self):
        del self.task_list[:]
        return