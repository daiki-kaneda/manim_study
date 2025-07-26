from manim import *

class Sentences(Scene):
    def __init__(self, sentences, max_lines=5, wait_time=1.0,is_tex = True, **kwargs):
        super().__init__(**kwargs)
        self.sentences = sentences
        self.max_lines = max_lines
        self.wait_time = wait_time
        self.is_tex = is_tex

    def construct(self):
        # VGroupは現在表示されているテキスト行を保持します
        lines = VGroup().to_edge(UL)

        for sentence_text in self.sentences:
            # 数式をサポートするためにMathTexを使用して新しいテキスト行を作成します
            # MathTex内では、通常のテキストは \text{} で囲むと良いです
            if self.is_tex:
                japanese_tex_template = TexTemplate(
    tex_compiler='xelatex', # ★ xelatex を明示的に指定
    output_format='.xdv',    # ★ PDF 出力が最も安定
    documentclass='\\documentclass[preview]{standalone}',
    preamble=r"""
        \usepackage{amsmath}
        \usepackage{amssymb}
        \usepackage{fontspec}    % ★ システムフォントを使うためのパッケージ
        \setmainfont{HannariMincho-Regular} % ★★★ あなたの環境での正確なPostScript名をここに記述 ★★★
                                     % 例: HiraginoSans-W3 (Macのヒラギノ角ゴ)
                                     % 例: YuGo-Medium (游ゴシック Medium)
        % \usepackage{zxjatype}   % 日本語組版ルールが必要な場合は追加 (フォント問題解決後)
        % \usepackage{pxjahyper}  % 日本語PDFのしおりなどが必要な場合は追加 (フォント問題解決後)
    """
)

                # new_line = MathTex(sentence_text, font_size=36,)                
                new_line = Tex(sentence_text,tex_template = japanese_tex_template,
                            
                               font_size=36,)                

            else:
                new_line = Text(sentence_text)

            # 行数が最大値に達した場合、最も古い行をフェードアウトさせます
            if len(lines) >= self.max_lines:
                self.play(FadeOut(lines[0], shift=UP * 0.5))
                lines.remove(lines[0])

            # 新しい行をVGroupに追加します
            lines.add(new_line)

            # すべての行を垂直に配置し、左端に揃えます
            lines.arrange(DOWN, aligned_edge=LEFT)
            lines.to_edge(UL)

            # 新しい行がフェードインするアニメーションを再生します
            self.play(FadeIn(new_line, shift=UP * 0.5))
            self.wait(self.wait_time)

        # シーンが終わる前に少し待ちます
        self.wait(2)

class ProofExample(Sentences):
    def __init__(self, **kwargs):
        proof_sentences = [
            r"\text{Let's prove that }\sqrt{2}\text{ is irrational.}",
            r"\text{1. Assume }\sqrt{2}\text{ is rational.}",
            r"\text{Then }\sqrt{2} = \frac{a}{b}\text{ for integers }a, b\text{ with no common factors.}",
            r"\text{2. Squaring both sides, we get }2 = \frac{a^2}{b^2}.",
            r"\text{3. So, }2b^2 = a^2.",
            r"\text{This means }a^2\text{ is even, so }a\text{ must be even.}",
            r"\text{4. Let }a = 2k\text{ for some integer }k.",
            r"\text{5. Then }2b^2 = (2k)^2 = 4k^2.",
            r"\text{6. So, }b^2 = 2k^2.",
            r"\text{This means }b^2\text{ is even, so }b\text{ must be even.}",
            r"\text{7. But we assumed }a\text{ and }b\text{ have no common factors.}",
            r"\text{This is a contradiction.}",
            r"\text{Therefore, }\sqrt{2}\text{ must be irrational.}",
        ]
        super().__init__(sentences=proof_sentences, max_lines=4, wait_time=2.5, **kwargs)

class ProofExampleJa(Sentences):
    def __init__(self, **kwargs):
        proof_sentences = [
            r"これから$\sqrt{2}$が無理数であることの証明をします。", # \text{} を削除し、数式を$で囲む
            r"1.$\sqrt{2}$ が有理数であると仮定します。",
            r"ここで、$\sqrt{2} = \frac{a}{b}$ ($a, b$は互いに素な自然数)", # \text{} を削除し、数式を$で囲む
            r"2. 両辺を二乗して、 $2 = \frac{a^2}{b^2}$.",
            r"3. よって, $2b^2 = a^2$.",
            r"これは$a^2$が偶数であることを意味し、従って、$a$も偶数でなくてはなりません。",
            r"4. $a = 2k$ とします ($k$は任意の整数)。",
            r"5. このとき、$2b^2 = (2k)^2 = 4k^2$ となります。",
            r"6. よって、$b^2 = 2k^2$ となります。",
            r"これは$b^2$が偶数であることを意味し、従って、$b$も偶数でなくてはなりません。",
            r"7. しかし、私たちは$a$と$b$が互いに素であると仮定しました。",
            r"これは矛盾です。",
            r"したがって、$\sqrt{2}$は無理数でなければなりません。",
        ]
        super().__init__(sentences=proof_sentences, max_lines=5, wait_time=2.5, **kwargs)

class NovelExample(Sentences):
    def __init__(self, **kwargs):
        wagahai_sentences = [
    "吾輩は猫である。",
    "名前はまだない。",
    "どこで生れたかとんと見当がつかぬ。",
    "何でも薄暗いじめじめした所でニャーニャー泣いていた事だけは記憶している。",
    "吾輩はここで始めて人間というものを見た。",
    "しかもあとで聞くとそれは書生という人間中で一番獰悪な種族であったそうだ。",
    "この書生というのは時々我々を捕えて煮て食うという話である。",
    "しかしその当時は何という考もなかったから別段恐しいとも思わなかった。",
    "ただ彼の掌に載せられてスーと持ち上げられた時何だかフワフワした感じがあったばかりである。",
    "掌の中で少し落ちついて書生の顔を見たのがいわゆる人間というものの見始であろう。",
    "この時妙なものだと思った感じが今でも残っている。",
    "それは毛というものをふさふさ生やした人間と違うてつるつるしたものであった。",
    "その上眼だけはからから光る。",
    "吾輩は眼を明けていられなかった。",
    "すると書生は我々を掌から急に地上へ卸ろした。",
    "静かにしていると、とんとん拍子に家の中へ案内された。",
    "今までと違い、暖かくていい匂いがした。",
    "吾輩は始めて人間というものの住む世界を知ったのである。",
    "この家で、吾輩は猫として生きていくことになった。",
    "それがどんな運命を辿るかは、まだ知る由もない。"
]
        super().__init__(sentences=wagahai_sentences, max_lines=4, wait_time=2.5,is_tex = False, **kwargs)
