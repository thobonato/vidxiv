from manim import *
import numpy as np

class TransformerAttentionDemo(Scene):
    def softmax(self, x):
        e = np.exp(x - np.max(x, axis=1, keepdims=True))
        return e / e.sum(axis=1, keepdims=True)

    def construct(self):
        # 1) Title
        title = Text("Transformer Self-Attention", font_size=48).to_edge(UP)
        self.play(Write(title))

        # 2) Tokens
        tokens = ["The", "cat", "sat", "on", "mat"]
        token_objs = VGroup(*[
            Rectangle(width=1.2, height=0.7, color=WHITE).set_fill(GRAY, 0.1)
            .add(Text(t, font_size=24))
            for t in tokens
        ]).arrange(RIGHT, buff=0.3).shift(UP * 1.5)
        for rect in token_objs:
            # center text
            rect[1].move_to(rect[0].get_center())
        self.play(*[FadeIn(mob) for mob in token_objs])

        # 3) Show Score Matrix = Q·K^T
        # random scores for demo
        scores = np.random.uniform(-1, 1, (5,5))
        score_matrix = Matrix(
            np.round(scores, 2).tolist(),
            left_bracket="[",
            right_bracket="]",
            v_buff=0.5,
        ).scale(0.7)
        score_matrix.next_to(token_objs, DOWN * 1.0).shift(LEFT * 2)
        score_label = MathTex("\\text{Scores} = QK^T", font_size=24).next_to(score_matrix, UP)
        self.play(Write(score_label))
        self.play(Create(score_matrix))

        # 4) Animate Softmax heatmap
        attn = self.softmax(scores)
        heatmap = VGroup()
        cell_size = 0.8
        for i in range(5):
            row = VGroup()
            for j in range(5):
                sq = Square(side_length=cell_size)
                # map weight to opacity 0.1–1
                alpha = 0.1 + 0.9 * attn[i,j]
                sq.set_fill(RED, alpha).set_stroke(width=0)
                row.add(sq)
            row.arrange(RIGHT, buff=0)
            heatmap.add(row)
        heatmap.arrange(DOWN, buff=0).next_to(score_matrix, RIGHT, buff=1.0)
        attn_label = MathTex("\\text{Attention} = \\text{softmax}(\\text{scores})", font_size=24).next_to(heatmap, UP)
        self.play(Write(attn_label))
        self.wait(0.5)
        # fade in each row
        for row in heatmap:
            self.play(FadeIn(row, run_time=0.3))
        self.wait(1)

        # 5) Multi-Head Attention overview
        self.play(FadeOut(score_matrix), FadeOut(heatmap))
        mh_title = Text("Multi-Head Attention", font_size=36).to_edge(UP)
        self.play(Transform(title, mh_title))

        # create 3 heads side by side
        heads = VGroup()
        for idx, color in zip(range(3), [BLUE, GREEN, YELLOW]):
            hm = heatmap.copy().set_opacity(1.0).set_color(color)
            hm.scale(0.6).shift(RIGHT * 3*(idx-1))
            heads.add(hm)
        self.play(*[FadeIn(h) for h in heads])

        # label them
        labels = VGroup(*[
            Text(f"Head {i+1}", font_size=20).next_to(heads[i], UP, buff=0.2)
            for i in range(3)
        ])
        self.play(*[Write(lbl) for lbl in labels])
        self.wait(1)

        # 6) Concatenate heads
        concat_arrow = Arrow(
            start=heads.get_bottom(), end=DOWN*2, buff=0, tip_length=0.2
        )
        concat_box = Rectangle(width=7, height=1.2, color=WHITE).set_fill(BLUE, 0.1)
        concat_box.next_to(concat_arrow, DOWN, buff=0)
        concat_text = Text("Concatenate & Linear ▶ Output", font_size=24).move_to(concat_box.get_center())
        self.play(GrowArrow(concat_arrow))
        self.play(Create(concat_box), Write(concat_text))
        self.wait(1)

        # 7) Show final contextual tokens
        ctx_tokens = VGroup(*[
            Rectangle(width=1.2, height=0.7, color=WHITE).set_fill(TEAL, 0.3)
            .add(Text(t, font_size=24))
            for t in tokens
        ]).arrange(RIGHT, buff=0.3).next_to(concat_box, DOWN, buff=1.0)
        for rect in ctx_tokens:
            rect[1].move_to(rect[0].get_center())
        self.play(*[FadeIn(m) for m in ctx_tokens])
        self.play(Write(Text("Contextualized Embeddings", font_size=24)
                        .next_to(ctx_tokens, DOWN)))
        self.wait(2)