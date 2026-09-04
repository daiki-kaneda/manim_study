from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import LessonScene


VALUES = [3, 1, 4, 1]
NO_DUP = [3, 1, 4, 2]
PAIRS = [
    (0, 1, 3, 1, False, r"3", r"1"),
    (0, 2, 3, 4, False, r"3", r"4"),
    (0, 3, 3, 1, False, r"3", r"1"),
    (1, 2, 1, 4, False, r"1", r"4"),
    (1, 3, 1, 1, True, r"1", r"1"),
    (2, 3, 4, 1, False, r"4", r"1"),
]


class FindDuplicate(LessonScene):
    """#1 巨大なリストに同じ値が 2 つあるか（約10分）"""

    def construct(self):
        self.header = self._open_header()
        self.part_question()
        self.part_trial_pairs()
        self.part_trial_double()
        self.part_step1_count()
        self.part_step2_seen()
        self.part_step3_index()
        self.part_example()
        self.part_generalize()
        self.part_summary()

    def _open_header(self):
        title = self._line(
            "巨大なリストに同じ値が",
            MathTex(r"2", font_size=40),
            "つあるか",
            font_size=36,
        )
        self._fit(title, 13.2)
        self.play(FadeIn(title), run_time=0.8)
        self.pause_new_screen()
        self.linger(1.5)
        self.play(title.animate.scale(0.52).to_edge(UP, buff=0.16), run_time=0.5)
        title.set_x(0)
        return title

    def part_question(self):
        fig = self._array_row(VALUES)
        cap = self.ja_text("4 つの数が、左からこの順に並んでいます。", font_size=22)
        pair = VGroup(fig, cap).arrange(DOWN, buff=0.28)
        pair.next_to(self.header, DOWN, buff=0.36)
        pair.set_x(0)
        self._nudge(pair)
        self.play(FadeIn(fig), run_time=0.8)
        self.pause_new_screen()
        self.play(FadeIn(cap), run_time=0.5)
        self.linger(cap.text)

        q1 = self.ja_text(
            "この 4 つの数の中に、同じ値が 2 回出ているでしょうか。",
            font_size=24,
        )
        self.stack_below(q1, pair, buff=0.32)
        q1.set_x(0)
        self._fit(q1, 13.0)
        q1.set_x(0)
        self.play(FadeIn(q1), run_time=0.5)
        self.linger(q1.text)

        q2 = self.ja_text(
            "同じ問いを、数が 100 万個ある列でも、間に合う持ち方はあるでしょうか。",
            font_size=24,
        )
        self.stack_below(q2, q1, buff=0.16)
        q2.set_x(0)
        self._fit(q2, 13.0)
        q2.set_x(0)
        self.play(FadeIn(q2), run_time=0.5)
        self.linger(q2.text, extra=0.35)

    def part_trial_pairs(self):
        chip = self.begin_step("試行  ペアを比べる", self.header)

        lead = self.ja_text(
            "まず、左から 2 つずつ組にして、値が同じかを全部比べてみます。",
            font_size=22,
        )
        self.below_chip(lead, chip, buff=0.22)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.5)
        self.linger(lead.text)

        arr = self._array_row(VALUES)
        self.stack_below(arr, lead, buff=0.36)
        arr.set_x(0)
        self.play(FadeIn(arr), run_time=0.6)
        self.pause_new_screen()

        counter = self._count_line(0)
        self.stack_below(counter, arr, buff=0.28)
        counter.set_x(0)
        self.play(FadeIn(counter), run_time=0.4)
        self.linger("比べた回数は 0 です。")

        cmp_mob = None
        for step, (i, j, _a, _b, same, left, right) in enumerate(PAIRS, start=1):
            self._reset_cells(arr)
            self._paint_cell(arr, i, YELLOW)
            self._paint_cell(arr, j, YELLOW)
            if same:
                word = "同じ"
                color = GREEN
            else:
                word = "違う"
                color = ORANGE
            nxt_cmp = self._line(
                MathTex(left, font_size=32, color=YELLOW),
                "と",
                MathTex(right, font_size=32, color=YELLOW),
                "は",
                self.ja_text(word, font_size=24, color=color),
                font_size=24,
            )
            nxt_cmp.next_to(counter, DOWN, buff=0.22)
            nxt_cmp.set_x(0)
            if cmp_mob is None:
                self.play(FadeIn(nxt_cmp), run_time=0.4)
            else:
                self.play(FadeOut(cmp_mob), run_time=0.25)
                self.play(FadeIn(nxt_cmp), run_time=0.4)
            cmp_mob = nxt_cmp
            self.linger(f"{_a} と {_b} は{word}。")

            nxt_counter = self._count_line(step)
            nxt_counter.move_to(counter)
            self.play(Transform(counter, nxt_counter), run_time=0.35)
            self.pause_short_formula()

        note1 = self.ja_text(
            "4 個の数なのに、比べた回数は 6 回でした。",
            font_size=22,
        )
        self.stack_below(note1, cmp_mob, buff=0.28)
        note1.set_x(0)
        self.play(FadeIn(note1), run_time=0.45)
        self.linger(note1.text)

        note2 = self.ja_text(
            "同じ値の 2 つは、5 回目で見つかりました。無いと言い切るには、残りも見る必要があります。",
            font_size=20,
        )
        self.stack_below(note2, note1, buff=0.12)
        note2.set_x(0)
        self._fit(note2, 13.0)
        note2.set_x(0)
        self.play(FadeIn(note2), run_time=0.45)
        self.linger(note2.text, extra=0.3)

    def part_trial_double(self):
        chip = self.begin_step("試行  倍にすると", self.header)

        lead = self.ja_text(
            "同じやり方で、列の長さを倍にしたら、比べる回数はどうなるでしょう。",
            font_size=22,
        )
        self.below_chip(lead, chip, buff=0.20)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.5)
        self.linger(lead.text)

        defn = self._line(
            "列の長さを",
            MathTex(r"n", font_size=28, color=YELLOW),
            "とおきます。いまは",
            MathTex(r"n=4", font_size=28, color=YELLOW),
            "でした。",
            font_size=22,
        )
        self.stack_below(defn, lead, buff=0.14)
        defn.set_x(0)
        self.play(FadeIn(defn), run_time=0.45)
        self.linger("列の長さを n とおきます。いまは n=4 でした。")

        intros = [
            self._line(
                MathTex(r"n=2", font_size=26),
                "のとき、組は 1 つだけ。個数",
                MathTex(r"1", font_size=26),
                font_size=20,
            ),
            self._line(
                MathTex(r"n=4", font_size=26),
                "のとき、いま数えた",
                MathTex(r"6", font_size=26),
                font_size=20,
            ),
            self._line(
                MathTex(r"n=8", font_size=26),
                "のとき、",
                MathTex(r"8\cdot 7/2=28", font_size=26),
                font_size=20,
            ),
            self._line(
                MathTex(r"n=16", font_size=26),
                "のとき、",
                MathTex(r"16\cdot 15/2=120", font_size=26),
                font_size=20,
            ),
        ]
        intro_block = self._formula_rows(intros, defn, buff=0.16, hold=self.PAUSE_SHORT_FORMULA)
        self.play(FadeOut(intro_block), run_time=0.35)

        table = self.aligned_table(
            [
                [
                    self._line("長さ", MathTex(r"n", font_size=22, color=GREY_B), font_size=18, color=GREY_B),
                    self.ja_text("ペアの個数", font_size=18, color=GREY_B),
                ],
                [MathTex(r"2", font_size=28), MathTex(r"1", font_size=28)],
                [MathTex(r"4", font_size=28), MathTex(r"6", font_size=28)],
                [MathTex(r"8", font_size=28), MathTex(r"28", font_size=28)],
                [MathTex(r"16", font_size=28), MathTex(r"120", font_size=28)],
            ],
            h_buff=0.50,
            v_buff=0.18,
        )
        table.scale(0.82)
        self.stack_below(table, defn, buff=0.20)
        table.set_x(0)
        self.reveal_table(table, row_wait=0.75)
        self.pause_complex()

        self.play(FadeOut(table), run_time=0.3)
        chart = self._pair_bars()
        self.stack_below(chart, defn, buff=0.18)
        chart.set_x(0)
        self._nudge(chart)
        self.play(FadeIn(chart), run_time=0.7)
        self.pause_new_screen()
        self.linger(2.2)

        notes = [
            self._line(
                "長さが",
                MathTex(r"4", font_size=24),
                "から",
                MathTex(r"8", font_size=24),
                "へ倍になると、回数は",
                MathTex(r"6", font_size=24),
                "から",
                MathTex(r"28", font_size=24),
                "へ、約",
                MathTex(r"4", font_size=24, color=YELLOW),
                "倍になります。",
                font_size=18,
            ),
            self._line(
                MathTex(r"8", font_size=24),
                "から",
                MathTex(r"16", font_size=24),
                "でも、",
                MathTex(r"28", font_size=24),
                "から",
                MathTex(r"120", font_size=24),
                "へ、また約",
                MathTex(r"4", font_size=24, color=YELLOW),
                "倍です。",
                font_size=18,
            ),
            self.ja_text(
                "100 万個だと、この増え方のままで間に合うのか、まだ式にしていません。",
                font_size=18,
            ),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, chart, buff=0.16)
            else:
                self.stack_below(mob, shown, buff=0.10)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.4)
            shown.add(mob)
            self.linger(2.4 if i < 2 else mob.text)

    def part_step1_count(self):
        chip = self.begin_step("STEP 1  ペアの個数", self.header)

        lead = self._line(
            "4 個のときに数えた 6 回を、長さ",
            MathTex(r"n", font_size=26, color=YELLOW),
            "の式にします。",
            font_size=22,
        )
        self.below_chip(lead, chip, buff=0.18)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.5)
        self.linger("4 個のときに数えた 6 回を、長さ n の式にします。")

        arr = self._array_row(VALUES)
        rights = [3, 2, 1, 0]
        tags = VGroup()
        for cell, k in zip(arr, rights):
            tag = MathTex(str(k), font_size=22, color=GOLD)
            tag.next_to(cell.box, DOWN, buff=0.12)
            tags.add(tag)
        fig = VGroup(arr, tags)
        self.stack_below(fig, lead, buff=0.28)
        fig.set_x(0)
        self.play(FadeIn(arr), run_time=0.5)
        for i, tag in enumerate(tags):
            self.play(FadeIn(tag), run_time=0.3)
            self.linger(1.1)
        cap = self.ja_text(
            "各マスの下は、その位置より右にあるマスの個数です。",
            font_size=18,
        )
        self.stack_below(cap, fig, buff=0.16)
        cap.set_x(0)
        self.play(FadeIn(cap), run_time=0.4)
        self.linger(cap.text)

        small = [
            MathTex(r"3+2+1+0", font_size=32),
            MathTex(r"=6", font_size=32, color=YELLOW),
        ]
        small_block = self._formula_rows(small, cap, buff=0.16, hold=self.PAUSE_SHORT_FORMULA)
        self.pause_conclusion()

        self.play(FadeOut(fig), FadeOut(cap), FadeOut(small_block), run_time=0.35)

        derived = [
            MathTex(r"(n-1)+(n-2)+\cdots+1+0", font_size=32),
            MathTex(r"=1+2+\cdots+(n-1)", font_size=32),
            self._line(
                MathTex(r"1", font_size=26),
                "から",
                MathTex(r"k", font_size=26, color=YELLOW),
                "までの和は",
                MathTex(r"\dfrac{k(k+1)}{2}", font_size=30),
                font_size=20,
            ),
            self._line(
                "ここで",
                MathTex(r"k=n-1", font_size=28, color=YELLOW),
                "とおく",
                font_size=20,
            ),
            MathTex(r"\dfrac{(n-1)((n-1)+1)}{2}=\dfrac{(n-1)n}{2}", font_size=32),
            MathTex(r"\dfrac{n(n-1)}{2}", font_size=40, color=YELLOW),
        ]
        der_block = self._formula_rows(derived, lead, buff=0.12, hold=self.PAUSE_COMPLEX)
        self.pause_conclusion()

        check = self._line(
            "検算:",
            MathTex(r"n=4", font_size=24),
            "なら",
            MathTex(r"\dfrac{4\cdot 3}{2}=6", font_size=24),
            "。",
            MathTex(r"n=8", font_size=24),
            "なら",
            MathTex(r"\dfrac{8\cdot 7}{2}=28", font_size=24),
            font_size=18,
        )
        self.stack_below(check, der_block, buff=0.14)
        check.set_x(0)
        self._fit(check, 13.0)
        check.set_x(0)
        self.play(FadeIn(check), run_time=0.4)
        self.linger("検算: n=4 なら 6。n=8 なら 28。")

        self.play(FadeOut(der_block), FadeOut(check), run_time=0.3)
        note = self._line(
            "この方法の仕事は、長さ",
            MathTex(r"n", font_size=26),
            "に対して",
            MathTex(r"\dfrac{n(n-1)}{2}", font_size=30, color=YELLOW),
            "回です。",
            font_size=20,
        )
        self.stack_below(note, lead, buff=0.22)
        note.set_x(0)
        self.play(FadeIn(note), run_time=0.45)
        self.linger("この方法の仕事は、長さ n に対して n(n-1)/2 回です。")
        self.pause_conclusion()

        ratio_lead = self.ja_text(
            "n が倍になると、この式はおよそ 4 倍になります。",
            font_size=20,
        )
        self.stack_below(ratio_lead, note, buff=0.16)
        ratio_lead.set_x(0)
        self.play(FadeIn(ratio_lead), run_time=0.4)
        self.linger(ratio_lead.text)

        ratio = [
            MathTex(r"\dfrac{2n(2n-1)}{2}=n(2n-1)", font_size=30),
            MathTex(r"\dfrac{n(n-1)}{2}", font_size=30),
            MathTex(r"\dfrac{2(2n-1)}{n-1}", font_size=32, color=YELLOW),
            self._line(
                MathTex(r"n=4", font_size=24),
                "を代入すると",
                MathTex(r"\dfrac{2(8-1)}{4-1}=\dfrac{14}{3}", font_size=26),
                font_size=18,
            ),
            self._line(
                MathTex(r"n", font_size=24),
                "が大きいと、この比は",
                MathTex(r"4", font_size=26, color=YELLOW),
                "に近づく",
                font_size=18,
            ),
        ]
        self._formula_rows(ratio, ratio_lead, buff=0.12, hold=self.PAUSE_COMPLEX)
        self.pause_conclusion()

    def part_step2_seen(self):
        chip = self.begin_step("STEP 2  見た値の箱", self.header)

        lead = self.ja_text(
            "全部のペアを作らなくても、いままでに見た値を箱に置いておけば足ります。",
            font_size=20,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.5)
        self.linger(lead.text)

        rules = [
            self._line(
                "いままでに見た値の集まりを",
                MathTex(r"\mathrm{Seen}", font_size=26, color=YELLOW),
                "とおく。最初は空",
                font_size=18,
            ),
            self._line(
                "配列を左から順に見て、今の値を",
                MathTex(r"x", font_size=26, color=GOLD),
                "とおく",
                font_size=18,
            ),
            self._line(
                MathTex(r"x", font_size=24, color=GOLD),
                "が",
                MathTex(r"\mathrm{Seen}", font_size=24, color=YELLOW),
                "にあれば、同じ値は 2 つある",
                font_size=18,
            ),
            self._line(
                "なければ",
                MathTex(r"x", font_size=24, color=GOLD),
                "を",
                MathTex(r"\mathrm{Seen}", font_size=24, color=YELLOW),
                "に入れる",
                font_size=18,
            ),
            self.ja_text("最後まで無ければ、同じ値は無い", font_size=18),
        ]
        rule_block = self._formula_rows(rules, lead, buff=0.10, hold=self.PAUSE_SHORT_FORMULA)
        self.pause_complex()
        self.play(FadeOut(rule_block), run_time=0.3)

        arr = self._array_row(VALUES)
        seen = self._seen_row([None, None, None, None])
        arr_lab = self.ja_text("配列", font_size=16, color=GREY_B)
        seen_lab = self.ja_text("見た値の箱", font_size=16, color=GREY_B)
        left = VGroup(arr_lab, arr).arrange(DOWN, buff=0.10)
        right = VGroup(seen_lab, seen).arrange(DOWN, buff=0.10)
        pair = VGroup(left, right).arrange(RIGHT, buff=0.70, aligned_edge=UP)
        self.stack_below(pair, lead, buff=0.20)
        pair.set_x(0)
        self._nudge(pair)
        self.play(FadeIn(pair), run_time=0.6)
        self.pause_new_screen()

        walk = [
            (0, [3, None, None, None], False, "x=3。箱は空なので、まだ無い。箱の 1 マス目に 3 を置く"),
            (1, [3, 1, None, None], False, "x=1。箱の中は 3 だけ。1 は無い。2 マス目に 1 を置く"),
            (2, [3, 1, 4, None], False, "x=4。箱の中は 3, 1。4 は無い。3 マス目に 4 を置く"),
            (3, [3, 1, 4, None], True, "x=1。箱の中に 1 がある。同じ値が 2 つある"),
        ]
        note = None
        for idx, filled, hit, text in walk:
            self._reset_cells(arr)
            self._paint_cell(arr, idx, YELLOW)
            nxt_seen = self._seen_row(filled, hit_value=1 if hit else None)
            nxt_seen.move_to(seen)
            self.play(FadeOut(seen), FadeIn(nxt_seen), run_time=0.45)
            seen = nxt_seen
            nxt_note = self.ja_text(text, font_size=18)
            nxt_note.next_to(pair, DOWN, buff=0.22)
            nxt_note.set_x(0)
            self._fit(nxt_note, 13.0)
            nxt_note.set_x(0)
            if note is None:
                self.play(FadeIn(nxt_note), run_time=0.4)
            else:
                self.play(FadeOut(note), run_time=0.22)
                self.play(FadeIn(nxt_note), run_time=0.4)
            note = nxt_note
            self.linger(text)

        close = [
            self.ja_text(
                "配列は 1 回だけ左から見ました。比べたのは、箱の中に今の値があるかどうかです。",
                font_size=18,
            ),
            self.ja_text("ペアは 6 組でしたが、見る位置は 4 つで足りました。", font_size=18),
        ]
        shown = VGroup()
        for i, mob in enumerate(close):
            if i == 0:
                self.stack_below(mob, note, buff=0.16)
            else:
                self.stack_below(mob, shown, buff=0.10)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.4)
            shown.add(mob)
            self.linger(mob.text)

        count_n = self._line(
            "列の長さを",
            MathTex(r"n", font_size=26, color=YELLOW),
            "とおく。この方法では、値を見る回数は",
            MathTex(r"n", font_size=28, color=GREEN),
            "回",
            font_size=20,
        )
        self.stack_below(count_n, shown, buff=0.16)
        count_n.set_x(0)
        self._fit(count_n, 13.0)
        count_n.set_x(0)
        self.play(FadeIn(count_n), run_time=0.45)
        self.linger("この方法では、値を見る回数は n 回です。")
        self.pause_conclusion()

    def part_step3_index(self):
        chip = self.begin_step("STEP 3  箱の番号", self.header)

        lead = self.ja_text(
            "箱の中を毎回端から探すと、また時間がかかります。値から箱の番号を決める持ち方があります。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.14)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.5)
        self.linger(lead.text)

        intro = self.ja_text(
            "値が 0 から 4 までしか出ないなら、番号そのものが箱です。",
            font_size=18,
        )
        self.stack_below(intro, lead, buff=0.12)
        intro.set_x(0)
        self.play(FadeIn(intro), run_time=0.4)
        self.linger(intro.text)

        marks = self._mark_row([False] * 5)
        self.stack_below(marks, intro, buff=0.28)
        marks.set_x(0)
        self.play(FadeIn(marks), run_time=0.55)
        self.pause_new_screen()

        mark_steps = [
            (3, [False, False, False, True, False], "x=3 を見たら、番号 3 のマスに印を付ける"),
            (1, [False, True, False, True, False], "x=1 を見たら、番号 1 のマスに印を付ける"),
            (4, [False, True, False, True, True], "x=4 を見たら、番号 4 のマスに印を付ける"),
            (1, [False, True, False, True, True], "次の x=1 では、番号 1 にすでに印がある。同じ値は 2 つある"),
        ]
        note = None
        for _x, flags, text in mark_steps:
            nxt = self._mark_row(flags, hit=1 if "すでに" in text else None)
            nxt.move_to(marks)
            self.play(FadeOut(marks), FadeIn(nxt), run_time=0.4)
            marks = nxt
            nxt_note = self.ja_text(text, font_size=18)
            nxt_note.next_to(marks, DOWN, buff=0.22)
            nxt_note.set_x(0)
            self._fit(nxt_note, 13.0)
            nxt_note.set_x(0)
            if note is None:
                self.play(FadeIn(nxt_note), run_time=0.4)
            else:
                self.play(FadeOut(note), run_time=0.22)
                self.play(FadeIn(nxt_note), run_time=0.4)
            note = nxt_note
            self.linger(text)

        mid = [
            self.ja_text("箱の番号が値そのものなので、探す必要がありません。", font_size=18),
            self.ja_text(
                "ただし、値が 100 万よりずっと大きい整数や、名前のような値だと、値の個数ぶんのマスは用意できません。",
                font_size=18,
            ),
        ]
        shown = VGroup()
        for i, mob in enumerate(mid):
            if i == 0:
                self.stack_below(mob, note, buff=0.14)
            else:
                self.stack_below(mob, shown, buff=0.08)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.4)
            shown.add(mob)
            self.linger(mob.text)

        self.play(
            FadeOut(intro),
            FadeOut(marks),
            FadeOut(note),
            FadeOut(shown),
            run_time=0.35,
        )

        hash_lead = [
            self._line(
                "箱の個数を",
                MathTex(r"m=5", font_size=26, color=YELLOW),
                "とおく",
                font_size=18,
            ),
            self._line(
                "値",
                MathTex(r"x", font_size=24, color=GOLD),
                "の箱の番号を、",
                MathTex(r"x", font_size=24, color=GOLD),
                "を",
                MathTex(r"m", font_size=24, color=YELLOW),
                "で割った余りとおく",
                font_size=18,
            ),
        ]
        hash_block = self._formula_rows(hash_lead, lead, buff=0.12, hold=self.PAUSE_SHORT_FORMULA)

        remainders = MathTex(
            r"3=5\cdot 0+3,\quad 1=5\cdot 0+1,\quad 4=5\cdot 0+4",
            font_size=28,
        )
        self.stack_below(remainders, hash_block, buff=0.14)
        remainders.set_x(0)
        self.play(FadeIn(remainders), run_time=0.5)
        self.pause_complex()

        hashed = self._mark_row([False] * 5)
        self.stack_below(hashed, remainders, buff=0.22)
        hashed.set_x(0)
        self.play(FadeIn(hashed), run_time=0.45)

        hash_walk = [
            ([False, False, False, True, False], "3 を 5 で割った余りは 3。番号 3 へ"),
            ([False, True, False, True, False], "1 を 5 で割った余りは 1。番号 1 へ"),
            ([False, True, False, True, True], "4 を 5 で割った余りは 4。番号 4 へ"),
            ([False, True, False, True, True], "次の 1 も余り 1。番号 1 にはすでに 1 がある"),
        ]
        hnote = None
        for flags, text in hash_walk:
            hit = 1 if "すでに" in text else None
            nxt = self._mark_row(flags, hit=hit, show_values=True)
            nxt.move_to(hashed)
            self.play(FadeOut(hashed), FadeIn(nxt), run_time=0.4)
            hashed = nxt
            nxt_note = self.ja_text(text, font_size=18)
            nxt_note.next_to(hashed, DOWN, buff=0.18)
            nxt_note.set_x(0)
            self._fit(nxt_note, 13.0)
            nxt_note.set_x(0)
            if hnote is None:
                self.play(FadeIn(nxt_note), run_time=0.35)
            else:
                self.play(FadeOut(hnote), run_time=0.2)
                self.play(FadeIn(nxt_note), run_time=0.35)
            hnote = nxt_note
            self.linger(text)

        names = [
            self.ja_text(
                "値から箱の番号を決める、この対応をハッシュと呼びます。",
                font_size=18,
            ),
            self.ja_text(
                "違う値が同じ番号になることもあります。その処理はこの問いでは使いません。今回は、番号が決まれば箱を直接見られる、というところまでです。",
                font_size=16,
            ),
        ]
        nshown = VGroup()
        for i, mob in enumerate(names):
            if i == 0:
                self.stack_below(mob, hnote, buff=0.12)
            else:
                self.stack_below(mob, nshown, buff=0.08)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.4)
            nshown.add(mob)
            self.linger(mob.text)

        warn1 = self.ja_text(
            "余りが同じだから値が同じ、ではありません。逆に、値が同じなら余りも同じ、です。",
            font_size=16,
            color=ORANGE,
        )
        self.stack_below(warn1, nshown, buff=0.10)
        warn1.set_x(0)
        self._fit(warn1, 13.0)
        warn1.set_x(0)
        self.play(FadeIn(warn1), run_time=0.4)
        self.linger(warn1.text)

        warn2 = self._line(
            "今回の 4 つの数では、同じ値",
            MathTex(r"1", font_size=22, color=GREEN),
            "だけが同じ箱に入りました。",
            font_size=16,
        )
        self.stack_below(warn2, warn1, buff=0.08)
        warn2.set_x(0)
        self.play(FadeIn(warn2), run_time=0.4)
        self.linger("今回の 4 つの数では、同じ値 1 だけが同じ箱に入りました。", extra=0.25)

    def part_example(self):
        chip = self.begin_step("実例", self.header)

        lead = self.ja_text(
            "同じ 4 つの数を、最初から最後までもう一度辿ります。",
            font_size=20,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        arr = self._array_row(VALUES)
        self.stack_below(arr, lead, buff=0.22)
        arr.set_x(0)
        self.play(FadeIn(arr), run_time=0.45)

        items = [
            (
                "ペア方式",
                self._line(
                    MathTex(r"3", font_size=22),
                    "と",
                    MathTex(r"1", font_size=22),
                    "、",
                    MathTex(r"3", font_size=22),
                    "と",
                    MathTex(r"4", font_size=22),
                    "、",
                    MathTex(r"3", font_size=22),
                    "と",
                    MathTex(r"1", font_size=22),
                    "、",
                    MathTex(r"1", font_size=22),
                    "と",
                    MathTex(r"4", font_size=22),
                    "、",
                    MathTex(r"1", font_size=22),
                    "と",
                    MathTex(r"1", font_size=22, color=GREEN),
                    "で同じ。回数",
                    MathTex(r"5", font_size=22),
                    "。最後までやると",
                    MathTex(r"6", font_size=22, color=YELLOW),
                    font_size=16,
                ),
            ),
            (
                "箱方式",
                self._line(
                    MathTex(r"3", font_size=22),
                    "を置く、",
                    MathTex(r"1", font_size=22),
                    "を置く、",
                    MathTex(r"4", font_size=22),
                    "を置く、次の",
                    MathTex(r"1", font_size=22, color=GREEN),
                    "は既にある。見る回数",
                    MathTex(r"4", font_size=22, color=GREEN),
                    font_size=16,
                ),
            ),
            (
                "個数の式",
                self._line(
                    "ペアは",
                    MathTex(r"\dfrac{4\cdot 3}{2}=6", font_size=24),
                    "。箱は",
                    MathTex(r"4", font_size=24),
                    font_size=16,
                ),
            ),
        ]
        shown = VGroup()
        for i, (tag, formula) in enumerate(items):
            tag_m = self.ja_text(tag, font_size=18, color=YELLOW)
            row = VGroup(tag_m, formula).arrange(RIGHT, buff=0.20)
            if i == 0:
                self.stack_below(row, arr, buff=0.22)
            else:
                self.stack_below(row, shown, buff=0.14)
            self._fit_left(row, 12.6)
            self.play(FadeIn(row), run_time=0.45)
            shown.add(row)
            self.linger(1.6)

        million = self._line(
            "100 万個: 列の長さ",
            MathTex(r"n=10^{6}", font_size=24, color=YELLOW),
            "とおく",
            font_size=18,
        )
        self.stack_below(million, shown, buff=0.16)
        million.set_x(0)
        self.play(FadeIn(million), run_time=0.4)
        self.linger("100 万個: 列の長さ n=10^6 とおく")

        mill_eq = [
            MathTex(r"10^{6}-1=999999", font_size=28),
            MathTex(r"\dfrac{10^{6}\times 999999}{2}=499999500000", font_size=28),
            self._line(
                "箱は",
                MathTex(r"10^{6}", font_size=26, color=GREEN),
                font_size=18,
            ),
        ]
        mill_block = self._formula_rows(mill_eq, million, buff=0.10, hold=self.PAUSE_COMPLEX)
        self.pause_conclusion()

        self.play(FadeOut(arr), FadeOut(shown), FadeOut(million), FadeOut(mill_block), run_time=0.3)

        clock = self.ja_text("1 秒に 1 億回比べられるとします。", font_size=20)
        self.stack_below(clock, lead, buff=0.20)
        clock.set_x(0)
        self.play(FadeIn(clock), run_time=0.4)
        self.linger(clock.text)

        times = [
            self._line(
                "ペア:",
                MathTex(r"499999500000\div 10^{8}=4999.995", font_size=26),
                "秒。およそ",
                MathTex(r"5000", font_size=26, color=ORANGE),
                "秒",
                font_size=18,
            ),
            self._line(
                "箱:",
                MathTex(r"10^{6}\div 10^{8}=0.01", font_size=26, color=GREEN),
                "秒",
                font_size=18,
            ),
        ]
        time_block = self._formula_rows(times, clock, buff=0.12, hold=self.PAUSE_COMPLEX)
        self.pause_conclusion()

        close = [
            self.ja_text("4 個なら、どちらの方法でもすぐ終わります。", font_size=18),
            self.ja_text(
                "100 万個では、ペアを全部作る持ち方は間に合いません。見た値の箱なら、長さと同じ回数で足ります。",
                font_size=18,
            ),
        ]
        cshown = VGroup()
        for i, mob in enumerate(close):
            if i == 0:
                self.stack_below(mob, time_block, buff=0.14)
            else:
                self.stack_below(mob, cshown, buff=0.08)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.4)
            cshown.add(mob)
            self.linger(mob.text)

        self.play(FadeOut(clock), FadeOut(time_block), FadeOut(cshown), run_time=0.3)
        same = self.ja_text(
            "同じ値が無い列も、同じ読み方で辿ります。新しい道具は使いません。",
            font_size=18,
        )
        self.stack_below(same, lead, buff=0.18)
        same.set_x(0)
        self.play(FadeIn(same), run_time=0.4)
        self.linger(same.text)

        arr2 = self._array_row(NO_DUP)
        self.stack_below(arr2, same, buff=0.18)
        arr2.set_x(0)
        self.play(FadeIn(arr2), run_time=0.4)

        none = [
            self._line(
                "箱に",
                MathTex(r"3,\ 1,\ 4,\ 2", font_size=24),
                "を順に置く。どれも初めて出る",
                font_size=18,
            ),
            self.ja_text("最後まで同じ値は無い", font_size=18),
            self._line(
                "ペア方式なら、無いと言い切るために",
                MathTex(r"\dfrac{4\cdot 3}{2}=6", font_size=26, color=YELLOW),
                "回全部必要",
                font_size=18,
            ),
        ]
        self._formula_rows(none, arr2, buff=0.12, hold=self.PAUSE_COMPLEX)
        self.pause_conclusion()

    def part_generalize(self):
        chip = self.begin_step("一般化", self.header)

        lines = [
            self.ja_text(
                "今やったことは、値から箱の番号を決めて、見た値を覚える、ということでした。",
                font_size=20,
            ),
            self.ja_text(
                "この持ち方を、ハッシュ表と呼びます。値の範囲が小さいときは、番号を値そのものにした印の配列でも同じ動きです。",
                font_size=18,
            ),
            self._line(
                "列の長さを",
                MathTex(r"n", font_size=26, color=YELLOW),
                "とおきます。ペアを全部比べる方法の仕事は",
                MathTex(r"\dfrac{n(n-1)}{2}", font_size=28),
                "回です。",
                font_size=18,
            ),
            self._line(
                "ハッシュ表（または印の配列）なら、値を見る回数は",
                MathTex(r"n", font_size=26, color=GREEN),
                "回です。その代わり、箱のための追加のメモリが要ります。",
                font_size=18,
            ),
        ]
        linger_texts = [
            "今やったことは、値から箱の番号を決めて、見た値を覚える、ということでした。",
            "この持ち方を、ハッシュ表と呼びます。値の範囲が小さいときは、番号を値そのものにした印の配列でも同じ動きです。",
            "列の長さを n とおきます。ペアを全部比べる方法の仕事は n(n-1)/2 回です。",
            "ハッシュ表なら、値を見る回数は n 回です。その代わり、箱のための追加のメモリが要ります。",
        ]
        shown = VGroup()
        for i, (mob, text) in enumerate(zip(lines, linger_texts)):
            if i == 0:
                self.below_chip(mob, chip, buff=0.22)
            else:
                self.stack_below(mob, shown, buff=0.14)
            self._fit_left(mob)
            self.play(FadeIn(mob), run_time=0.5)
            shown.add(mob)
            self.linger(text)

        growth = [
            self.ja_text(
                "n が大きくなったときの仕事の増え方を、型として書くことがあります。",
                font_size=18,
            ),
            self._line(
                "ペア方式は、だいたい",
                MathTex(r"n^{2}", font_size=24),
                "に比例します。この型を",
                MathTex(r"O(n^{2})", font_size=26, color=ORANGE),
                "と書きます。",
                font_size=18,
            ),
            self._line(
                "箱方式は、だいたい",
                MathTex(r"n", font_size=24),
                "に比例します。この型を",
                MathTex(r"O(n)", font_size=26, color=GREEN),
                "と書きます。",
                font_size=18,
            ),
        ]
        gblock = VGroup()
        for i, mob in enumerate(growth):
            if i == 0:
                self.stack_below(mob, shown, buff=0.18)
            else:
                self.stack_below(mob, gblock, buff=0.10)
            self._fit_left(mob)
            self.play(FadeIn(mob), run_time=0.45)
            gblock.add(mob)
            self.linger(2.2)

        ts = MathTex(
            r"T_{\mathrm{pair}}(n)=\dfrac{n(n-1)}{2},\qquad T_{\mathrm{seen}}(n)=n",
            font_size=30,
            color=YELLOW,
        )
        self.stack_below(ts, gblock, buff=0.18)
        ts.set_x(0)
        self._fit(ts, 12.8)
        ts.set_x(0)
        self.play(Write(ts), run_time=1.0)
        self.pause_conclusion()

        bigo = MathTex(
            r"T_{\mathrm{pair}}(n)=O(n^{2}),\qquad T_{\mathrm{seen}}(n)=O(n)",
            font_size=30,
            color=YELLOW,
        )
        self.stack_below(bigo, ts, buff=0.14)
        bigo.set_x(0)
        self.play(Write(bigo), run_time=0.9)
        self.pause_conclusion()

        mem = self._line(
            "追加メモリ",
            MathTex(r"=O(n)", font_size=28, color=GOLD),
            font_size=20,
        )
        self.stack_below(mem, bigo, buff=0.14)
        mem.set_x(0)
        self.play(FadeIn(mem), run_time=0.4)
        self.linger("追加メモリは O(n) です。")
        self.pause_conclusion()

        trade = [
            self.ja_text("時間を短くする代わりに、箱のメモリを使っています。", font_size=18),
            self.ja_text("値が同じかを知る、という問いでは、この交換が効きます。", font_size=18),
        ]
        tshown = VGroup()
        for i, mob in enumerate(trade):
            if i == 0:
                self.stack_below(mob, mem, buff=0.12)
            else:
                self.stack_below(mob, tshown, buff=0.08)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.4)
            tshown.add(mob)
            self.linger(mob.text)

    def part_summary(self):
        chip = self.begin_step("まとめ", self.header)

        rows = [
            self._line(
                "全てのペアを比べると、回数は",
                MathTex(r"\dfrac{n(n-1)}{2}", font_size=26),
                "で、",
                MathTex(r"n", font_size=24),
                "が倍だとおよそ",
                MathTex(r"4", font_size=24),
                "倍",
                font_size=20,
            ),
            self.ja_text("見た値を箱に置くと、配列は 1 回見るだけで足りる", font_size=20),
            self.ja_text(
                "値から箱の番号を決める持ち方が、ハッシュ表（範囲が小さいときは印の配列）",
                font_size=20,
            ),
            self._line(
                "仕事の増え方の型は、ペアが",
                MathTex(r"O(n^{2})", font_size=24, color=ORANGE),
                "、箱が",
                MathTex(r"O(n)", font_size=24, color=GREEN),
                "。箱には追加メモリ",
                MathTex(r"O(n)", font_size=24, color=GOLD),
                "が要る",
                font_size=20,
            ),
        ]
        shown = VGroup()
        for i, mob in enumerate(rows):
            if i == 0:
                self.below_chip(mob, chip, buff=0.28)
            else:
                self.stack_below(mob, shown, buff=0.22)
            self._fit_left(mob)
            self.play(FadeIn(mob), run_time=0.5)
            shown.add(mob)
            self.linger(1.7)

        related = self.ja_text(
            "名簿の重複や、同じ番号が二度出ていないかの検査でも、同じ持ち方が使えます。",
            font_size=18,
            color=GREY_B,
        )
        self.stack_below(related, shown, buff=0.32)
        self._fit_left(related)
        self.play(FadeIn(related), run_time=0.45)
        self.linger(related.text, extra=0.45)

    def _array_row(self, values, highlights=None, side=0.95):
        cells = VGroup()
        for i, value in enumerate(values):
            color = BLUE
            width = 3.0
            if highlights and i in highlights:
                color = YELLOW
                width = 4.5
            cell = self._indexed_cell(value, i, color=color, side=side, stroke_width=width)
            cells.add(cell)
        cells.arrange(RIGHT, buff=0.18)
        self._align_boxes(cells)
        return cells

    def _indexed_cell(self, value, index, color=BLUE, side=0.95, stroke_width=3.0, empty=False, hit=False):
        box = RoundedRectangle(
            width=side,
            height=side,
            corner_radius=0.12,
            color=GREEN if hit else color,
            stroke_width=4.5 if hit else stroke_width,
            fill_color=GREEN if hit else color,
            fill_opacity=0.22 if hit else 0.14,
        )
        idx = MathTex(str(index), font_size=18, color=GREY_B)
        idx.next_to(box, UP, buff=0.10)
        parts = [idx, box]
        if not empty and value is not None:
            lab = MathTex(str(value), font_size=32)
            lab.move_to(box)
            parts.append(lab)
        g = VGroup(*parts)
        g.box = box
        g.idx = idx
        return g

    def _seen_row(self, values, hit_value=None, side=0.90):
        cells = VGroup()
        for i, value in enumerate(values):
            empty = value is None
            hit = (not empty) and hit_value is not None and value == hit_value
            cell = self._indexed_cell(
                value,
                i + 1,
                color=TEAL,
                side=side,
                empty=empty,
                hit=hit,
            )
            cells.add(cell)
        cells.arrange(RIGHT, buff=0.16)
        self._align_boxes(cells)
        return cells

    def _mark_row(self, flags, hit=None, show_values=False, side=0.85):
        cells = VGroup()
        stored = {1: 1, 3: 3, 4: 4}
        for i, marked in enumerate(flags):
            is_hit = hit is not None and i == hit and marked
            box = RoundedRectangle(
                width=side,
                height=side,
                corner_radius=0.12,
                color=GREEN if is_hit else (GOLD if marked else GREY_B),
                stroke_width=4.5 if is_hit else (3.2 if marked else 2.2),
                fill_color=GREEN if is_hit else (GOLD if marked else GREY_B),
                fill_opacity=0.28 if is_hit else (0.20 if marked else 0.06),
            )
            idx = MathTex(str(i), font_size=18, color=GREY_B)
            idx.next_to(box, UP, buff=0.10)
            parts = [idx, box]
            if marked:
                if show_values and i in stored:
                    lab = MathTex(str(stored[i]), font_size=28)
                else:
                    lab = MathTex(r"\checkmark", font_size=28, color=GREEN if is_hit else GOLD)
                lab.move_to(box)
                parts.append(lab)
            g = VGroup(*parts)
            g.box = box
            g.idx = idx
            cells.add(g)
        cells.arrange(RIGHT, buff=0.16)
        self._align_boxes(cells)
        return cells

    def _align_boxes(self, cells):
        if len(cells) < 2:
            return cells
        anchor = cells[0].box
        for cell in cells[1:]:
            cell.box.align_to(anchor, UP)
            cell.idx.next_to(cell.box, UP, buff=0.10)
            extras = [m for m in cell.submobjects if m is not cell.box and m is not cell.idx]
            for extra in extras:
                extra.move_to(cell.box)
        return cells

    def _paint_cell(self, row, index, color):
        cell = row[index]
        self.play(
            cell.box.animate.set_color(color).set_stroke(width=4.5),
            run_time=0.28,
        )

    def _reset_cells(self, row, color=BLUE):
        anims = []
        for cell in row:
            anims.append(cell.box.animate.set_color(color).set_stroke(width=3.0))
        if anims:
            self.play(*anims, run_time=0.22)

    def _count_line(self, n):
        return self._line(
            "比べた回数",
            MathTex(rf"={n}", font_size=32, color=YELLOW),
            font_size=22,
        )

    def _pair_bars(self):
        ns = (2, 4, 8, 16)
        heights = (1, 6, 28, 120)
        max_h = 120.0
        chart_h = 2.8
        bar_w = 0.55
        gap = 0.55
        origin = ORIGIN
        y_axis = Line(origin, origin + UP * chart_h, color=GREY_B, stroke_width=2)
        x_axis = Line(origin, origin + RIGHT * 4.6, color=GREY_B, stroke_width=2)
        ticks = VGroup()
        for val in (0, 30, 60, 90, 120):
            y = chart_h * (val / max_h)
            tick = Line(LEFT * 0.08, RIGHT * 0.08, color=GREY_B, stroke_width=1.5)
            tick.move_to(origin + UP * y)
            lab = MathTex(str(val), font_size=16, color=GREY_B)
            lab.next_to(tick, LEFT, buff=0.10)
            ticks.add(VGroup(tick, lab))
        y_label = self.ja_text("ペアの個数", font_size=16)
        y_title = VGroup(self.ja_text("縦", font_size=16, color=GREY_B), y_label).arrange(RIGHT, buff=0.08)
        y_title.next_to(y_axis, LEFT, buff=0.85)
        y_title.align_to(y_axis, UP)
        bars = VGroup()
        x_labs = VGroup()
        for i, (n, h) in enumerate(zip(ns, heights)):
            bh = max(chart_h * (h / max_h), 0.06)
            bar = Rectangle(
                width=bar_w,
                height=bh,
                color=BLUE,
                fill_color=BLUE,
                fill_opacity=0.75,
                stroke_width=1.5,
            )
            x = 0.70 + i * (bar_w + gap)
            bar.move_to(origin + RIGHT * x + UP * (bh / 2))
            nlab = MathTex(str(n), font_size=20)
            nlab.next_to(bar, DOWN, buff=0.12)
            bars.add(bar)
            x_labs.add(nlab)
        x_title = VGroup(
            self.ja_text("横", font_size=16, color=GREY_B),
            MathTex(r"n", font_size=20),
        ).arrange(RIGHT, buff=0.08)
        x_title.next_to(x_axis, DOWN, buff=0.42)
        x_title.align_to(x_axis, RIGHT)
        group = VGroup(y_axis, x_axis, ticks, bars, x_labs, y_title, x_title)
        return group

    def _line(self, *chunks, font_size=24, color=None, buff=0.08):
        parts = []
        for chunk in chunks:
            if isinstance(chunk, str):
                kw = {"font_size": font_size}
                if color is not None:
                    kw["color"] = color
                parts.append(self.ja_text(chunk, **kw))
            else:
                parts.append(chunk)
        return VGroup(*parts).arrange(RIGHT, buff=buff)

    def _formula_rows(self, rows, under, buff=0.36, hold=None):
        if hold is None:
            hold = self.PAUSE_COMPLEX
        block = VGroup(*rows).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        self.stack_below(block, under, buff=buff)
        block.set_x(0)
        self._fit(block, 12.6)
        block.set_x(0)
        for row in block:
            self.play(FadeIn(row), run_time=self.PAUSE_REWRITE)
            super().wait(hold)
        return block

    def _fit(self, mob, max_w=12.4):
        if mob.width > max_w:
            mob.scale_to_fit_width(max_w)
        return mob

    def _fit_left(self, mob, max_w=12.2):
        left = mob.get_left().copy()
        self._fit(mob, max_w)
        mob.shift(left - mob.get_left())
        return mob

    def _nudge(self, mob):
        frame_left = -config.frame_width / 2 + 0.08
        overflow = frame_left - mob.get_left()[0]
        if overflow > 0:
            mob.shift(RIGHT * overflow)
        frame_right = config.frame_width / 2 - 0.08
        over_r = mob.get_right()[0] - frame_right
        if over_r > 0:
            mob.shift(LEFT * over_r)
        return mob
