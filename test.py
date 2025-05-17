from manim import *

class IntroScene(Scene):
    def construct(self):
        # animation for: Simple diagram: Input sequence (blocks A, B, C, D) -> RNN node (processing A) -> node (processing B + A state) -> ... (sequential chain).
        input_sequence = VGroup(
            Square(side_length=0.8, fill_color=BLUE, fill_opacity=0.8).set_stroke(color=WHITE).add(Text("A").scale(0.7)),
            Square(side_length=0.8, fill_color=BLUE, fill_opacity=0.8).set_stroke(color=WHITE).add(Text("B").scale(0.7)),
            Square(side_length=0.8, fill_color=BLUE, fill_opacity=0.8).set_stroke(color=WHITE).add(Text("C").scale(0.7)),
            Square(side_length=0.8, fill_color=BLUE, fill_opacity=0.8).set_stroke(color=WHITE).add(Text("D").scale(0.7))
        ).arrange(RIGHT, buff=0.2)

        rnn_nodes = VGroup(
            Circle(radius=0.5, fill_color=RED, fill_opacity=0.8).set_stroke(color=WHITE).add(Text("RNN").scale(0.5)),
            Circle(radius=0.5, fill_color=RED, fill_opacity=0.8).set_stroke(color=WHITE).add(Text("RNN").scale(0.5)),
            Circle(radius=0.5, fill_color=RED, fill_opacity=0.8).set_stroke(color=WHITE).add(Text("RNN").scale(0.5)),
            Circle(radius=0.5, fill_color=RED, fill_opacity=0.8).set_stroke(color=WHITE).add(Text("RNN").scale(0.5))
        ).arrange(RIGHT, buff=1).shift(DOWN*2)

        rnn_arrows = VGroup(
            Arrow(input_sequence[0].get_bottom(), rnn_nodes[0].get_top()),
            Arrow(input_sequence[1].get_bottom(), rnn_nodes[1].get_top()),
            Arrow(input_sequence[2].get_bottom(), rnn_nodes[2].get_top()),
            Arrow(input_sequence[3].get_bottom(), rnn_nodes[3].get_top()),
            Arrow(rnn_nodes[0].get_right(), rnn_nodes[1].get_left()),
            Arrow(rnn_nodes[1].get_right(), rnn_nodes[2].get_left()),
            Arrow(rnn_nodes[2].get_right(), rnn_nodes[3].get_left())
        )

        self.play(FadeIn(input_sequence), FadeIn(rnn_nodes), Create(rnn_arrows))
        self.wait(1)

        # animation for: Highlight the arrow chain in the RNN diagram to show sequential dependency.
        sequential_arrows = VGroup(
            rnn_arrows[4], rnn_arrows[5], rnn_arrows[6]
        )
        self.play(sequential_arrows.animate.set_color(YELLOW).set_stroke(width=4))
        self.wait(1)

        self.play(FadeOut(VGroup(input_sequence, rnn_nodes, rnn_arrows, sequential_arrows)))

        # animation for: Simple diagram: Input sequence -> CNN layer (small kernel) -> another layer... Arrows show limited receptive field requiring depth.
        cnn_input_sequence = VGroup(
            Square(side_length=0.5, fill_color=BLUE, fill_opacity=0.8).set_stroke(color=WHITE),
            Square(side_length=0.5, fill_color=BLUE, fill_opacity=0.8).set_stroke(color=WHITE),
            Square(side_length=0.5, fill_color=BLUE, fill_opacity=0.8).set_stroke(color=WHITE),
            Square(side_length=0.5, fill_color=BLUE, fill_opacity=0.8).set_stroke(color=WHITE),
            Square(side_length=0.5, fill_color=BLUE, fill_opacity=0.8).set_stroke(color=WHITE),
            Square(side_length=0.5, fill_color=BLUE, fill_opacity=0.8).set_stroke(color=WHITE)
        ).arrange(RIGHT, buff=0.1)

        cnn_layer1 = VGroup(
            Square(side_length=0.5, fill_color=GREEN, fill_opacity=0.8).set_stroke(color=WHITE),
            Square(side_length=0.5, fill_color=GREEN, fill_opacity=0.8).set_stroke(color=WHITE),
            Square(side_length=0.5, fill_color=GREEN, fill_opacity=0.8).set_stroke(color=WHITE),
            Square(side_length=0.5, fill_color=GREEN, fill_opacity=0.8).set_stroke(color=WHITE)
        ).arrange(RIGHT, buff=0.1).shift(DOWN*1.5)

        cnn_layer2 = VGroup(
            Square(side_length=0.5, fill_color=PURPLE, fill_opacity=0.8).set_stroke(color=WHITE),
            Square(side_length=0.5, fill_color=PURPLE, fill_opacity=0.8).set_stroke(color=WHITE)
        ).arrange(RIGHT, buff=0.1).shift(DOWN*3)

        cnn_arrows1 = VGroup(
            Arrow(cnn_input_sequence[0].get_bottom(), cnn_layer1[0].get_top()),
            Arrow(cnn_input_sequence[1].get_bottom(), cnn_layer1[0].get_top()),
            Arrow(cnn_input_sequence[1].get_bottom(), cnn_layer1[1].get_top()),
            Arrow(cnn_input_sequence[2].get_bottom(), cnn_layer1[1].get_top()),
            Arrow(cnn_input_sequence[2].get_bottom(), cnn_layer1[2].get_top()),
            Arrow(cnn_input_sequence[3].get_bottom(), cnn_layer1[2].get_top()),
            Arrow(cnn_input_sequence[3].get_bottom(), cnn_layer1[3].get_top()),
            Arrow(cnn_input_sequence[4].get_bottom(), cnn_layer1[3].get_top())
        )

        cnn_arrows2 = VGroup(
            Arrow(cnn_layer1[0].get_bottom(), cnn_layer2[0].get_top()),
            Arrow(cnn_layer1[1].get_bottom(), cnn_layer2[0].get_top()),
            Arrow(cnn_layer1[1].get_bottom(), cnn_layer2[1].get_top()),
            Arrow(cnn_layer1[2].get_bottom(), cnn_layer2[1].get_top())
        )

        self.play(FadeIn(cnn_input_sequence), FadeIn(cnn_layer1), FadeIn(cnn_layer2), Create(cnn_arrows1), Create(cnn_arrows2))
        self.wait(1)

        # animation for: Annotate diagrams showing long paths between early inputs and late outputs.
        long_path_rnn = VGroup(
            Arrow(input_sequence[0].get_bottom(), rnn_nodes[0].get_top(), buff=0),
            Arrow(rnn_nodes[0].get_right(), rnn_nodes[1].get_left(), buff=0),
            Arrow(rnn_nodes[1].get_right(), rnn_nodes[2].get_left(), buff=0),
            Arrow(rnn_nodes[2].get_right(), rnn_nodes[3].get_left(), buff=0)
        ).set_color(RED).set_stroke(width=4)

        long_path_cnn = VGroup(
            Arrow(cnn_input_sequence[0].get_bottom(), cnn_layer1[0].get_top(), buff=0),
            Arrow(cnn_layer1[0].get_bottom(), cnn_layer2[0].get_top(), buff=0)
        ).set_color(RED).set_stroke(width=4)

        self.play(
            FadeOut(VGroup(cnn_arrows1, cnn_arrows2)),
            FadeIn(long_path_cnn)
        )
        self.wait(1)
        self.play(FadeOut(VGroup(cnn_input_sequence, cnn_layer1, cnn_layer2, long_path_cnn)))
        self.wait(1)


class IntroScene2(Scene):
    def construct(self):
        # animation for: Simple diagram: Input sequence (blocks A, B, C, D) -> RNN node (processing A) -> node (processing B + A state) -> ... (sequential chain).

        # Create input sequence
        input_labels = ["A", "B", "C", "D"]
        input_blocks = VGroup(*[
            Square(side_length=0.8, fill_opacity=0.8, fill_color=BLUE)
            for _ in input_labels
        ]).arrange(RIGHT, buff=0.1)

        for block, label_text in zip(input_blocks, input_labels):
            label = Text(label_text, font_size=24).move_to(block)
            block.add(label)

        # Create RNN nodes (simplified)
        rnn_nodes = VGroup(*[
            Circle(radius=0.4, fill_opacity=0.8, fill_color=RED)
            for _ in input_labels
        ]).arrange(RIGHT, buff=1.5).next_to(input_blocks, DOWN, buff=1.0)

        # Create sequential arrows
        rnn_arrows = VGroup()
        # Input to first node
        arrow_in1 = Arrow(input_blocks[0].get_bottom(), rnn_nodes[0].get_top(), buff=0.1)
        rnn_arrows.add(arrow_in1)
        # Sequential dependencies between nodes
        for i in range(len(rnn_nodes) - 1):
            arrow_seq = Arrow(rnn_nodes[i].get_right(), rnn_nodes[i+1].get_left(), buff=0.1)
            rnn_arrows.add(arrow_seq)
            # Input to subsequent nodes
            arrow_in = Arrow(input_blocks[i+1].get_bottom(), rnn_nodes[i+1].get_top(), buff=0.1)
            rnn_arrows.add(arrow_in)

        rnn_diagram = VGroup(input_blocks, rnn_nodes, rnn_arrows).move_to(LEFT * 3)

        self.play(
            Create(input_blocks),
            LaggedStart(*[Create(node) for node in rnn_nodes], lag_ratio=0.5),
            LaggedStart(*[Create(arrow) for arrow in rnn_arrows], lag_ratio=0.1),
            run_time=3
        )

        # animation for: Highlight the arrow chain in the RNN diagram to show sequential dependency.
        sequential_path_arrows = VGroup(arrow_in1, rnn_arrows[1], rnn_arrows[2], rnn_arrows[4], rnn_arrows[5]) # Specific arrows showing sequential flow
        self.play(
            LaggedStart(*[arrow.animate.set_color(YELLOW).set_stroke(width=6) for arrow in sequential_path_arrows], lag_ratio=0.2),
            run_time=2
        )
        self.wait(1)

        # animation for: Simple diagram: Input sequence -> CNN layer (small kernel) -> another layer... Arrows show limited receptive field requiring depth.

        # Clear previous scene elements
        self.play(FadeOut(rnn_diagram, sequential_path_arrows))

        # Use the same input blocks
        input_blocks_cnn = input_blocks.copy().move_to(LEFT * 3 + UP * 1.5)

        # Create CNN layers (simplified)
        layer1_nodes = VGroup(*[
            Square(side_length=0.6, fill_opacity=0.8, fill_color=GREEN)
            for _ in range(3) # Represents output nodes from a small kernel
        ]).arrange(RIGHT, buff=0.2).next_to(input_blocks_cnn, DOWN, buff=0.8)

        layer2_nodes = VGroup(*[
            Square(side_length=0.6, fill_opacity=0.8, fill_color=TEAL)
            for _ in range(2) # Even smaller output
        ]).arrange(RIGHT, buff=0.3).next_to(layer1_nodes, DOWN, buff=0.8)

        # Create CNN connections (local)
        cnn_arrows = VGroup()
        # Input to Layer 1 (kernel size ~2)
        cnn_arrows.add(Arrow(input_blocks_cnn[0].get_bottom(), layer1_nodes[0].get_top(), buff=0.1))
        cnn_arrows.add(Arrow(input_blocks_cnn[1].get_bottom(), layer1_nodes[0].get_top(), buff=0.1))
        cnn_arrows.add(Arrow(input_blocks_cnn[1].get_bottom(), layer1_nodes[1].get_top(), buff=0.1))
        cnn_arrows.add(Arrow(input_blocks_cnn[2].get_bottom(), layer1_nodes[1].get_top(), buff=0.1))
        cnn_arrows.add(Arrow(input_blocks_cnn[2].get_bottom(), layer1_nodes[2].get_top(), buff=0.1))
        cnn_arrows.add(Arrow(input_blocks_cnn[3].get_bottom(), layer1_nodes[2].get_top(), buff=0.1))

        # Layer 1 to Layer 2 (kernel size ~2)
        cnn_arrows.add(Arrow(layer1_nodes[0].get_bottom(), layer2_nodes[0].get_top(), buff=0.1))
        cnn_arrows.add(Arrow(layer1_nodes[1].get_bottom(), layer2_nodes[0].get_top(), buff=0.1))
        cnn_arrows.add(Arrow(layer1_nodes[1].get_bottom(), layer2_nodes[1].get_top(), buff=0.1))
        cnn_arrows.add(Arrow(layer1_nodes[2].get_bottom(), layer2_nodes[1].get_top(), buff=0.1))

        cnn_diagram = VGroup(input_blocks_cnn, layer1_nodes, layer2_nodes, cnn_arrows).move_to(RIGHT * 3)

        self.play(
            FadeIn(input_blocks_cnn),
            Create(layer1_nodes),
            Create(layer2_nodes),
            LaggedStart(*[Create(arrow) for arrow in cnn_arrows], lag_ratio=0.05),
            run_time=3
        )
        self.wait(1)


        # animation for: Annotate diagrams showing long paths between early inputs and late outputs.

        # Annotate RNN: Path from A to D's processing node
        path_rnn = VMobject()
        start_point_rnn = input_blocks[0].get_bottom()
        rnn_points = [
            start_point_rnn,
            rnn_nodes[0].get_top(),
            rnn_nodes[0].get_right(),
            rnn_nodes[1].get_left(),
            rnn_nodes[1].get_right(),
            rnn_nodes[2].get_left(),
            rnn_nodes[2].get_right(),
            rnn_nodes[3].get_left()
        ]
        path_rnn.set_points_as_corners(rnn_points)
        path_rnn.set_stroke(color=YELLOW, width=4, opacity=0.7)

        # Annotate CNN: Path from A to the last output node (requires traversing layers)
        path_cnn = VMobject()
        start_point_cnn = input_blocks_cnn[0].get_bottom()
        cnn_points = [
            start_point_cnn,
            layer1_nodes[0].get_top(),
            layer1_nodes[0].get_bottom(),
            layer2_nodes[0].get_top()
            # This is a simplified path. A true path from A to *the* last output element's
            # representation would be longer and more complex, potentially going
            # through multiple nodes in each layer. Let's illustrate a representative
            # path from an early input to a late output element's representation.
            # Let's go from A (input 0) to the last node in Layer 2 (node 1).
            # A -> L1_0 -> L2_0 -> L2_1 (impossible direct). Must go A -> L1_0/L1_1 -> L2_1
            # A -> L1_0 -> L2_0 -> something... Let's connect A to L1_0, then L1_0 to L2_0,
            # and show that L2_0 only sees A and B. To get A to affect L2_1 (D input),
            # need A->L1_x->L2_1. Let's trace a path that shows depth.
            # A -> L1_0 (influenced by A, B) -> L2_0 (influenced by L1_0, L1_1)
            # D -> L1_2 (influenced by C, D) -> L2_1 (influenced by L1_1, L1_2)
            # To link A and D, need A->...->L1_1->...->L2_1
            # Let's draw A to L1_0, then L1_0 to L2_0, and D to L1_2, then L1_2 to L2_1.
            # Then show a path connecting L2_0 and L2_1 requires more interaction/depth (conceptually).
            # Alternative: Draw a long path from A to L2_1.
            # A -> L1_0 -> L2_0 -> Need more layers or different kernels...
            # Let's just draw A to L1_0 and D to L1_2 to show locality first.
            # Then a path from A to L2_1 showing it must traverse multiple steps/layers.
        ]
        path_cnn = VMobject()
        # Path from A (input 0) through L1_0 to L2_0 (local path)
        cnn_local_path_1 = VMobject().set_points_as_corners([
            input_blocks_cnn[0].get_bottom(),
            layer1_nodes[0].get_top(),
            layer1_nodes[0].get_bottom(),
            layer2_nodes[0].get_top()
        ]).set_stroke(color=BLUE, width=4, opacity=0.7)

        # Path from D (input 3) through L1_2 to L2_1 (local path)
        cnn_local_path_2 = VMobject().set_points_as_corners([
            input_blocks_cnn[3].get_bottom(),
            layer1_nodes[2].get_top(),
            layer1_nodes[2].get_bottom(),
            layer2_nodes[1].get_top()
        ]).set_stroke(color=BLUE, width=4, opacity=0.7)

        # Illustrate a long-range path from A to L2_1 (conceptually showing need for depth)
        cnn_long_path = VMobject().set_points_as_corners([
            input_blocks_cnn[0].get_bottom(),
            layer1_nodes[0].get_top(), # Via L1_0
            layer1_nodes[0].get_right() + RIGHT * 0.5, # Across L1
            layer1_nodes[2].get_top() + UP * 0.5,
            layer1_nodes[2].get_bottom(), # Towards L2_1 via L1_2
            layer2_nodes[1].get_top()
        ]).set_stroke(color=YELLOW, width=4, opacity=0.7).set_dash_style([0.2, 0.1])


        self.play(Create(path_rnn), run_time=2)
        self.wait(1) # Wait after annotating RNN

        # Need to bring RNN diagram back for the transition or show both side-by-side
        # Let's position both side-by-side initially.
        self.play(
             rnn_diagram.animate.shift(LEFT*3), # Shift RNN slightly left if needed
             cnn_diagram.animate.shift(RIGHT*3), # Shift CNN slightly right if needed
             FadeIn(path_rnn), # Ensure RNN path is visible if it was faded out
             FadeIn(cnn_diagram), # Ensure CNN diagram is visible
             run_time=0.1 # Instant re-positioning
        )
        self.remove(rnn_diagram, sequential_path_arrows) # Clean up original RNN diagram if moved

        # Recreate and position RNN diagram for side-by-side
        input_blocks_rnn_side = VGroup(*[
            Square(side_length=0.8, fill_opacity=0.8, fill_color=BLUE)
            for _ in input_labels
        ]).arrange(RIGHT, buff=0.1)
        for block, label_text in zip(input_blocks_rnn_side, input_labels):
            label = Text(label_text, font_size=24).move_to(block)
            block.add(label)
        rnn_nodes_side = VGroup(*[
            Circle(radius=0.4, fill_opacity=0.8, fill_color=RED)
            for _ in input_labels
        ]).arrange(RIGHT, buff=1.5).next_to(input_blocks_rnn_side, DOWN, buff=1.0)
        rnn_arrows_side = VGroup()
        arrow_in1_side = Arrow(input_blocks_rnn_side[0].get_bottom(), rnn_nodes_side[0].get_top(), buff=0.1)
        rnn_arrows_side.add(arrow_in1_side)
        for i in range(len(rnn_nodes_side) - 1):
            arrow_seq_side = Arrow(rnn_nodes_side[i].get_right(), rnn_nodes_side[i+1].get_left(), buff=0.1)
            rnn_arrows_side.add(arrow_seq_side)
            arrow_in_side = Arrow(input_blocks_rnn_side[i+1].get_bottom(), rnn_nodes_side[i+1].get_top(), buff=0.1)
            rnn_arrows_side.add(arrow_in_side)
        rnn_diagram_side = VGroup(input_blocks_rnn_side, rnn_nodes_side, rnn_arrows_side).move_to(LEFT * 3)
        # Recreate the RNN path for the side-by-side version
        path_rnn_side = VMobject()
        rnn_points_side = [
            input_blocks_rnn_side[0].get_bottom(), rnn_nodes_side[0].get_top(),
            rnn_nodes_side[0].get_right(), rnn_nodes_side[1].get_left(),
            rnn_nodes_side[1].get_right(), rnn_nodes_side[2].get_left(),
            rnn_nodes_side[2].get_right(), rnn_nodes_side[3].get_left()
        ]
        path_rnn_side.set_points_as_corners(rnn_points_side)
        path_rnn_side.set_stroke(color=YELLOW, width=4, opacity=0.7)


        # Recreate and position CNN diagram for side-by-side
        input_blocks_cnn_side = input_blocks.copy().move_to(LEFT*0.5 + UP * 1.5) # Adjust position
        layer1_nodes_side = VGroup(*[
            Square(side_length=0.6, fill_opacity=0.8, fill_color=GREEN)
            for _ in range(3)
        ]).arrange(RIGHT, buff=0.2).next_to(input_blocks_cnn_side, DOWN, buff=0.8)
        layer2_nodes_side = VGroup(*[
            Square(side_length=0.6, fill_opacity=0.8, fill_color=TEAL)
            for _ in range(2)
        ]).arrange(RIGHT, buff=0.3).next_to(layer1_nodes_side, DOWN, buff=0.8)
        cnn_arrows_side = VGroup()
        cnn_arrows_side.add(Arrow(input_blocks_cnn_side[0].get_bottom(), layer1_nodes_side[0].get_top(), buff=0.1))
        cnn_arrows_side.add(Arrow(input_blocks_cnn_side[1].get_bottom(), layer1_nodes_side[0].get_top(), buff=0.1))
        cnn_arrows_side.add(Arrow(input_blocks_cnn_side[1].get_bottom(), layer1_nodes_side[1].get_top(), buff=0.1))
        cnn_arrows_side.add(Arrow(input_blocks_cnn_side[2].get_bottom(), layer1_nodes_side[1].get_top(), buff=0.1))
        cnn_arrows_side.add(Arrow(input_blocks_cnn_side[2].get_bottom(), layer1_nodes_side[2].get_top(), buff=0.1))
        cnn_arrows_side.add(Arrow(input_blocks_cnn_side[3].get_bottom(), layer1_nodes_side[2].get_top(), buff=0.1))
        cnn_arrows_side.add(Arrow(layer1_nodes_side[0].get_bottom(), layer2_nodes_side[0].get_top(), buff=0.1))
        cnn_arrows_side.add(Arrow(layer1_nodes_side[1].get_bottom(), layer2_nodes_side[0].get_top(), buff=0.1))
        cnn_arrows_side.add(Arrow(layer1_nodes_side[1].get_bottom(), layer2_nodes_side[1].get_top(), buff=0.1))
        cnn_arrows_side.add(Arrow(layer1_nodes_side[2].get_bottom(), layer2_nodes_side[1].get_top(), buff=0.1))
        cnn_diagram_side = VGroup(input_blocks_cnn_side, layer1_nodes_side, layer2_nodes_side, cnn_arrows_side).move_to(RIGHT * 2.5) # Adjust position

        # Recreate the CNN long path annotation
        cnn_long_path_side = VMobject().set_points_as_corners([
            input_blocks_cnn_side[0].get_bottom(), # A
            layer1_nodes_side[0].get_top(), # via L1_0
            layer1_nodes_side[0].get_right() + RIGHT * 0.3, # Across L1
            layer1_nodes_side[2].get_top() + UP * 0.3,
            layer1_nodes_side[2].get_bottom(), # Towards L2_1 via L1_2 connection
            layer2_nodes_side[1].get_top() # To L2_1
        ]).set_stroke(color=YELLOW, width=4, opacity=0.7).set_dash_style([0.2, 0.1])


        self.play(
            FadeOut(rnn_diagram), # Fade out initial centered diagrams
            FadeOut(cnn_diagram),
            FadeIn(rnn_diagram_side), # Fade in side-by-side diagrams
            FadeIn(cnn_diagram_side),
            Create(path_rnn_side), # Re-create and show RNN path
            Create(cnn_long_path_side), # Create and show CNN long path
            run_time=3
        )
        self.wait(2) # Wait longer to let the viewer see both diagrams and paths

        self.wait(1)
