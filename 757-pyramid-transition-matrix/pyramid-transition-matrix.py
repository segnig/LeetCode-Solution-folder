class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        tops = defaultdict(list)
        for key in allowed:
            tops[key[:2]].append(key[2])

        def gen_next_rows(full_items, all_valid=set(), i=0, cur=''):
            if any([item == [] for item in full_items]):
                return []

            if i == len(full_items):
                all_valid.add(cur)
                return

            for item in full_items[i]:
                gen_next_rows(full_items, all_valid, i + 1, cur + item)

            return all_valid

        seen = set()

        def find_next_row(last):
            n = len(last)
            if n == 1:
                return True

            options = gen_next_rows([tops[last[i:i + 2]] for i in range(n - 1)], set())

            for option in options:
                if option in seen:
                    continue
                if find_next_row(option):
                    return True
                seen.add(option)
            return False
        return find_next_row(bottom)