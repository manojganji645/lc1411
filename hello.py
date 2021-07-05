from manimlib.imports import *
from manimlib.animation.movement import MoveAlongPath
from manimlib.utils.config_ops import digest_config

class SquareToCircle(GraphScene):
    def __init__(self, *args, **kwargs):
        GraphScene.__init__(self, *args, **kwargs)
        self.valid_ex = None
        self.blocks = None
        self.positions = None
    def display_text(self, text):
        title = TextMobject(text)
        title.set_color(BLUE)
        title.shift(DOWN)
        self.add(title)
        self.wait(3)
        self.play(FadeOut(title))
    def construct(self):
        self.blocks = [
            [RED,   GREEN,  RED],
            [RED,   BLUE,   RED],
            [GREEN, BLUE,   GREEN],
            [GREEN, RED,    GREEN],
            [BLUE,  GREEN,  BLUE],
            [BLUE,  RED,    BLUE],
            [RED,   GREEN,  BLUE],
            [RED,   BLUE,   GREEN],
            [GREEN, BLUE,   RED],
            [GREEN, RED,    BLUE],
            [BLUE,  GREEN,  RED],
            [BLUE,  RED,    GREEN],
        ]
        self.positions = [
            np.array((-5, 3, 0)),
            np.array((-3, 3, 0)),
            np.array((-1, 3, 0)),
            np.array((1, 3, 0)),
            np.array((3, 3, 0)),
            np.array((5, 3, 0)),
            np.array((-5, 2, 0)),
            np.array((-3, 2, 0)),
            np.array((-1, 2, 0)),
            np.array((1, 2, 0)),
            np.array((3, 2, 0)),
            np.array((5, 2, 0)),
        ]
        random.seed(0)
        self.display_text("Leetcode 1411 : Number of Ways to Paint N × 3 Grid")

        self.display_text("First, lets look at the simple case of $n=1$")
        self.base_case()
        self.clear()
        nbs = []
        sbs = []
        for t in zip(self.blocks, self.positions):
            nb, sb = get_block(t[0], t[1])
            nbs.append(nb)
            sbs.append(sb)
        for i in range(0, 12, 1):
            self.add(sbs[i])

        self.display_text("These are 12 possible paintings for $n=1$\linebreak"\
                            " Lets number each of the 12 blocks from 0 to 11")
        self.display_text("Now, lets try to construct all possible paintings "\
                        "for $n=2$\linebreak It can be seen as placing one of the 12"\
                        " blocks over the other\linebreak")
        ''' Also 2nd block depends only"\
                        " on the 1st block\linebreak Similar argument can be applied "\
                        "for placement of $n$th block\linebreak which depends only on "\
                        "$(n-1)$th block.'''
        self.clear()

        self.valid_case()

        self.clear()
        self.display_text("For $n=2$, we can iterate through all the possible combinations\linebreak and check if two "\
                        "blocks can fit together. This calculation will \linebreak take "\
                        "144(12*12) block comparison operations\linebreak"\
                        " We can store this information as edges $(i, j)$\linebreak"\
                        " where $i$th block can be painted adjacent to $j$th block")
        self.display_text("Lets try $n=3$ now")
        for i in range(0, 12, 1):
            self.add(sbs[i])
        self.valid_ex.move_to(np.array((-4.5,0,0)))
        self.add(self.valid_ex)
        t = TextMobject("This is one of the possible\linebreak paintings for $n=2$")
        t.shift(3*RIGHT)
        self.play(Write(t))
        self.wait(5)
        self.remove(t)
        t = TextMobject("Lets check which of these above\linebreak blocks can be placed at $n=3$\linebreak for this sample painting")
        t.shift(3*RIGHT)
        self.play(Write(t))
        self.wait(5)
        fadelist = []
        for i in range(len(self.blocks)):
            if self.blocks[i][0]==self.blocks[2][0] or self.blocks[i][1]==self.blocks[2][1] \
                    or self.blocks[i][2]==self.blocks[2][2]:
                fadelist.append(sbs[i])
                sbs[i].fade(darkness=0.8)
        self.remove(t)
        t = TextMobject("Only above highlighted blocks\linebreak can be placed at $n=3$")
        t.shift(3*RIGHT)
        self.play(Write(t))
        self.wait(5)
        self.remove(t)
        t = TextMobject("We can see that 3rd block only\linebreak depends on the 2nd block\linebreak"\
                        " but not on the 1st block because\linebreak"\
                        "1st block is not in contact with 3rd block")
        t.shift(2*RIGHT)
        self.play(Write(t))
        self.wait(5)
        self.remove(t)
        self.clear()
        def local_display1(txt, height=1):
            t = TextMobject(txt)
            self.play(Write(t))
            self.wait(5)
            self.remove(t)
        local_display1("Till now, we made some important observations\linebreak"\
                        " Each row of any valid painting will be one of the 12 blocks\linebreak"\
                        " which we have seen\linebreak" \
                        " Each row of painting dependents only on its previous row\linebreak"\
                        " This observation has a profound implication that\linebreak"\
                        " we can always keep track of number of solutions with just \linebreak"\
                        " their last block which is nothing but 12 states"
                        )
        local_display1("We are going to use these observations to construct\linebreak"\
                        " a bottom-up solution. We have solutions for $n=1$ and $2$\linebreak"\
                        " Now, we try to get number of solutions for $n$ \linebreak"\
                        " if we know number of solutions for $(n-1)$")
        local_display1("Let $a_{n-1,i}$ be number of paitings of $(n-1)$ rows\linebreak"\
                        " which are painted $i$th block in $(n-1)$th row\linebreak"\
                        " Any $a_{n,i}$ can be calculated from summing up $a_{n-1,j}$'s \linebreak"\
                        " where there is an edge $(i,j)$ present")
        local_display1("Pseudo code can be as follows...\linebreak")
        t = TextMobject("Create an array $a$ of size $n*12$\linebreak"\
                        " Populate $1$st row with all $1$'s\linebreak"\
                        " for m : $2$ to n\linebreak"\
                        " for every edge$(i, j)$\linebreak"\
                        " $a_{m, i} += a_{m-1, j}$\linebreak"\
                        " $a_{m, j} += a_{m-1, i}$\linebreak"\
                        )
        sr = SurroundingRectangle(t, color=WHITE)
        self.add(t)
        self.add(sr)
        self.wait(10)


    def valid_case(self):
        nb1, sb = get_block(self.blocks[0], self.positions[0])
        nb1.shift(UP)
        self.play(FadeIn(nb1))
        nb2, sb = get_block(self.blocks[2], self.positions[2])
        self.play(FadeIn(nb2))
        vg = VGroup(nb1, nb2)
        self.valid_ex = vg
        path = Line(start = vg.get_center(), end=vg.get_center()-np.array((3,0,0)))
        self.play(MoveAlongPath(vg, path))
        
        content = TextMobject("This is a valid painting")
        content.set_color(GREEN)
        content.shift(2*RIGHT)
        self.play(Write(content))
        self.wait(2)

        vg = VGroup(vg, content)
        path = Line(start = vg.get_center(), end=vg.get_center()+np.array((0,2,0)))
        self.play(MoveAlongPath(vg, path))

        nb1, sb = get_block(self.blocks[0], self.positions[0])
        self.play(FadeIn(nb1))
        nb2, sb = get_block(self.blocks[1], self.positions[1])
        nb2.shift(DOWN)
        self.play(FadeIn(nb2))
        vg = VGroup(nb1, nb2)
        path = Line(start = vg.get_center(), end=vg.get_center()-np.array((3,0,0)))
        self.play(MoveAlongPath(vg, path))
        
        content = TextMobject("This is not a valid painting")
        content.shift(2*RIGHT)
        content.set_color(RED)
        self.play(Write(content))
        self.wait(2)
    def base_case(self):
        sq2 = Rectangle(height=0.5, width=0.5)
        sq2.move_to(np.array((0, 3.5, 0)))
        sq1 = sq2.deepcopy()
        sq3 = sq2.deepcopy()
        sq1.shift(0.5*LEFT)
        sq3.shift(0.5*RIGHT)
        vg = VGroup(sq1, sq2, sq3)
        self.play(FadeIn(vg))
        
        vg1 = vg.deepcopy()
        vg1.shift(1.5*DOWN+4*LEFT)
        vg1[0].set_fill(RED, opacity=0.5)
        arrow1 = Arrow(start=vg.get_bottom(), end = vg1.get_top(), tip_length=0.2)
        self.play(GrowArrow(arrow1))
        self.play(FadeIn(vg1))
        
        vg2 = vg.deepcopy()
        vg2.shift(1.5*DOWN)
        vg2[0].set_fill(GREEN, opacity=0.5)
        arrow2 = Arrow(start=vg.get_bottom(), end = vg2.get_top(), tip_length=0.2)
        self.play(GrowArrow(arrow2))
        self.play(FadeIn(vg2))

        vg3 = vg.deepcopy()
        vg3.shift(1.5*DOWN-4*LEFT)
        vg3[0].set_fill(BLUE, opacity=0.5)
        arrow1 = Arrow(start=vg.get_bottom(), end = vg3.get_top(), tip_length=0.2)
        self.play(GrowArrow(arrow1))
        self.play(FadeIn(vg3))

        vg4 = vg1.deepcopy()
        vg4.move_to(np.array((-5,0,0)))
        vg4[1].set_fill(GREEN, opacity=0.5)
        print(vg1.get_bottom(), vg4.get_top())
        arrow1 = Arrow(start=vg1.get_bottom(), end = vg4.get_top(), tip_length=0.2)
        self.play(GrowArrow(arrow1))
        self.play(FadeIn(vg4))

        vg5 = vg1.deepcopy()
        vg5.move_to(np.array((-3,0,0)))
        vg5[1].set_fill(BLUE, opacity=0.5)
        print(vg1.get_bottom(), vg5.get_top())
        arrow2 = Arrow(start=vg1.get_bottom(), end = vg5.get_top(), tip_length=0.2)
        self.play(GrowArrow(arrow2))
        self.play(FadeIn(vg5))

        vg6 = vg2.deepcopy()
        vg6.move_to(np.array((-1,0,0)))
        vg6[1].set_fill(RED, opacity=0.5)
        arrow1 = Arrow(start=vg2.get_bottom(), end = vg6.get_top(), tip_length=0.2)
        self.play(GrowArrow(arrow1))
        self.play(FadeIn(vg6))

        vg7 = vg2.deepcopy()
        vg7.move_to(np.array((1,0,0)))
        vg7[1].set_fill(BLUE, opacity=0.5)
        arrow2 = Arrow(start=vg2.get_bottom(), end = vg7.get_top(), tip_length=0.2)
        self.play(GrowArrow(arrow2))
        self.play(FadeIn(vg7))

        vg8 = vg3.deepcopy()
        vg8.move_to(np.array((3,0,0)))
        vg8[1].set_fill(RED, opacity=0.5)
        arrow1 = Arrow(start=vg3.get_bottom(), end = vg8.get_top(), tip_length=0.2)
        self.play(GrowArrow(arrow1))
        self.play(FadeIn(vg8))

        vg9 = vg3.deepcopy()
        vg9.move_to(np.array((5,0,0)))
        vg9[1].set_fill(GREEN, opacity=0.5)
        arrow2 = Arrow(start=vg3.get_bottom(), end = vg9.get_top(), tip_length=0.2)
        self.play(GrowArrow(arrow2))
        self.play(FadeIn(vg9))

        t = TextMobject("Real estate problems now!! :P").move_to(np.array((0, -3.5, 0)))
        self.add(t)

        vg10 = vg4.deepcopy()
        vg10.shift(2*DOWN+0.5*LEFT)
        vg10.rotate(3* TAU/4)
        vg10[2].set_fill(RED, opacity=0.5)
        arrow2 = Arrow(start=vg4.get_bottom(), end=vg10.get_top(), tip_length=0.2)
        self.play(GrowArrow(arrow2))
        self.play(FadeIn(vg10))

        vg11 = vg4.deepcopy()
        vg11.shift(2*DOWN-0.5*LEFT)
        vg11.rotate(3 * TAU/4)
        vg11[2].set_fill(BLUE, opacity=0.5)
        arrow2 = Arrow(start=vg4.get_bottom(), end=vg11.get_top(), tip_length=0.2)
        self.play(GrowArrow(arrow2))
        self.play(FadeIn(vg11))

        self.play(FadeOut(t))
        
        vg12 = vg5.deepcopy()
        vg12.shift(2*DOWN+0.5*LEFT)
        vg12.rotate(3*TAU/4)
        vg12[2].set_fill(RED, opacity=0.5)
        arrow2 = Arrow(start=vg5.get_bottom(), end=vg12.get_top(), tip_length=0.2)
        self.play(GrowArrow(arrow2))
        self.play(FadeIn(vg12))

        vg13 = vg5.deepcopy()
        vg13.shift(2*DOWN-0.5*LEFT)
        vg13.rotate(3*TAU/4)
        vg13[2].set_fill(GREEN, opacity=0.5)
        arrow2 = Arrow(start=vg5.get_bottom(), end=vg13.get_top(), tip_length=0.2)
        self.play(GrowArrow(arrow2))
        self.play(FadeIn(vg13))

        vg14 = vg6.deepcopy()
        vg14.shift(2*DOWN+0.5*LEFT)
        vg14.rotate(3* TAU/4)
        vg14[2].set_fill(GREEN, opacity=0.5)
        arrow2 = Arrow(start=vg6.get_bottom(), end=vg14.get_top(), tip_length=0.2)
        self.play(GrowArrow(arrow2))
        self.play(FadeIn(vg14))

        vg15 = vg6.deepcopy()
        vg15.shift(2*DOWN-0.5*LEFT)
        vg15.rotate(3 * TAU/4)
        vg15[2].set_fill(BLUE, opacity=0.5)
        arrow2 = Arrow(start=vg6.get_bottom(), end=vg15.get_top(), tip_length=0.2)
        self.play(GrowArrow(arrow2))
        self.play(FadeIn(vg15))

        vg16 = vg7.deepcopy()
        vg16.shift(2*DOWN+0.5*LEFT)
        vg16.rotate(3*TAU/4)
        vg16[2].set_fill(RED, opacity=0.5)
        arrow2 = Arrow(start=vg7.get_bottom(), end=vg16.get_top(), tip_length=0.2)
        self.play(GrowArrow(arrow2))
        self.play(FadeIn(vg16))

        vg17 = vg7.deepcopy()
        vg17.shift(2*DOWN-0.5*LEFT)
        vg17.rotate(3*TAU/4)
        vg17[2].set_fill(GREEN, opacity=0.5)
        arrow2 = Arrow(start=vg7.get_bottom(), end=vg17.get_top(), tip_length=0.2)
        self.play(GrowArrow(arrow2))
        self.play(FadeIn(vg17))


        vg18 = vg8.deepcopy()
        vg18.shift(2*DOWN+0.5*LEFT)
        vg18.rotate(3* TAU/4)
        vg18[2].set_fill(GREEN, opacity=0.5)
        arrow2 = Arrow(start=vg8.get_bottom(), end=vg18.get_top(), tip_length=0.2)
        self.play(GrowArrow(arrow2))
        self.play(FadeIn(vg18))

        vg19 = vg8.deepcopy()
        vg19.shift(2*DOWN-0.5*LEFT)
        vg19.rotate(3 * TAU/4)
        vg19[2].set_fill(BLUE, opacity=0.5)
        arrow2 = Arrow(start=vg8.get_bottom(), end=vg19.get_top(), tip_length=0.2)
        self.play(GrowArrow(arrow2))
        self.play(FadeIn(vg19))

        vg20 = vg9.deepcopy()
        vg20.shift(2*DOWN+0.5*LEFT)
        vg20.rotate(3*TAU/4)
        vg20[2].set_fill(RED, opacity=0.5)
        arrow2 = Arrow(start=vg9.get_bottom(), end=vg20.get_top(), tip_length=0.2)
        self.play(GrowArrow(arrow2))
        self.play(FadeIn(vg20))

        vg21 = vg9.deepcopy()
        vg21.shift(2*DOWN-0.5*LEFT)
        vg21.rotate(3*TAU/4)
        vg21[2].set_fill(BLUE, opacity=0.5)
        arrow2 = Arrow(start=vg9.get_bottom(), end=vg21.get_top(), tip_length=0.2)
        self.play(GrowArrow(arrow2))
        self.play(FadeIn(vg21))

        self.wait(2)




        



def get_block(colors, position):
    ns = [Rectangle(height=1, width=1, color=color) for color in colors]
    ns = [x[0].set_fill(x[1], opacity=0.5) for x in zip(ns, colors)]
    ns[0].shift(LEFT)
    ns[2].shift(RIGHT)
    normal_block = VGroup(*ns)
    
    ss = [Rectangle(height=0.5, width=0.5, color=color) for color in colors]
    ss = [x[0].set_fill(x[1], opacity=0.5) for x in zip(ss, colors)]
    ss[0].shift(0.5*LEFT)
    ss[2].shift(0.5*RIGHT)
    small_block = VGroup(*ss)
    small_block.move_to(position)
    
    return normal_block, small_block
