from anytree import Node, RenderTree 
from anytree.exporter import DotExporter
PassUpNode4422067792 = Node('TranslationUnit*_7792')
PassUpNode4421926224 = Node('TranslationUnit*_6224', parent=PassUpNode4422067792)
PassUpNode4421923984 = Node('TranslationUnit*_3984', parent=PassUpNode4421926224)
PassUpNode4421923344 = Node('TranslationUnit*_3344', parent=PassUpNode4421923984)
Declaration4421923152 = Node('Declaration_3152', parent=PassUpNode4421923344)
DeclarationSpecifiers4420570512 = Node('DeclarationSpecifiers_0512', parent=Declaration4421923152)
leaf = Node('int_0512', parent=DeclarationSpecifiers4420570512)
InitDeclList4420570576 = Node('InitDeclList_0576', parent=Declaration4421923152)
Identifier4421548368 = Node('Identifier_8368', parent=InitDeclList4420570576)
leaf = Node('var0_8368', parent=Identifier4421548368)
leaf = Node("Type=['int'], TokenLocation=(1, 4, 5)", parent=Identifier4421548368)
Declaration4421923408 = Node('Declaration_3408', parent=PassUpNode4421923344)
DeclarationSpecifiers4421678608 = Node('DeclarationSpecifiers_8608', parent=Declaration4421923408)
leaf = Node('char_8608', parent=DeclarationSpecifiers4421678608)
InitDeclList4421923216 = Node('InitDeclList_3216', parent=Declaration4421923408)
Identifier4421923280 = Node('Identifier_3280', parent=InitDeclList4421923216)
leaf = Node('var1_3280', parent=Identifier4421923280)
leaf = Node("Type=['char'], TokenLocation=(2, 15, 6)", parent=Identifier4421923280)
Declaration4421923920 = Node('Declaration_3920', parent=PassUpNode4421923984)
DeclarationSpecifiers4421923536 = Node('DeclarationSpecifiers_3536', parent=Declaration4421923920)
leaf = Node('int_3536', parent=DeclarationSpecifiers4421923536)
InitDeclList4421923664 = Node('InitDeclList_3664', parent=Declaration4421923920)
FunctionPrototype4421923792 = Node('FunctionPrototype_3792', parent=InitDeclList4421923664)
Identifier4421923472 = Node('Identifier_3472', parent=FunctionPrototype4421923792)
leaf = Node('fun1_3472', parent=Identifier4421923472)
leaf = Node("Return Type=['int'], Subtype='Function Prototype', Label='fun1', Arguments=[{'Type': ['int']}, {'Type': ['char']}], TokenLocation=(6, 56, 5)", parent=Identifier4421923472)
PassUpNode4421923600 = Node('ParameterList*_3600', parent=FunctionPrototype4421923792)
DeclarationSpecifiers4421923728 = Node('DeclarationSpecifiers_3728', parent=PassUpNode4421923600)
leaf = Node('int_3728', parent=DeclarationSpecifiers4421923728)
DeclarationSpecifiers4421923856 = Node('DeclarationSpecifiers_3856', parent=PassUpNode4421923600)
leaf = Node('char_3856', parent=DeclarationSpecifiers4421923856)
FunctionDefintion4421924880 = Node('FunctionDefintion_4880', parent=PassUpNode4421926224)
DeclarationSpecifiers4421924112 = Node('DeclarationSpecifiers_4112', parent=FunctionDefintion4421924880)
leaf = Node('int_4112', parent=DeclarationSpecifiers4421924112)
FunctionPrototype4421924496 = Node('FunctionPrototype_4496', parent=FunctionDefintion4421924880)
Identifier4421924176 = Node('Identifier_4176', parent=FunctionPrototype4421924496)
leaf = Node('main_4176', parent=Identifier4421924176)
leaf = Node("Subtype='Function Prototype', Label='main', Arguments=[{'Type Qualifier': ['const'], 'Type': ['int']}, {'Type': ['char']}], TokenLocation=(9, 101, 5)", parent=Identifier4421924176)
PassUpNode4421924816 = Node('ParameterList*_4816', parent=FunctionPrototype4421924496)
Declaration4421924432 = Node('Declaration_4432', parent=PassUpNode4421924816)
DeclarationSpecifiers4421924304 = Node('DeclarationSpecifiers_4304', parent=Declaration4421924432)
leaf = Node('const_4304', parent=DeclarationSpecifiers4421924304)
DeclarationSpecifiers4421924368 = Node('DeclarationSpecifiers_4368', parent=DeclarationSpecifiers4421924304)
leaf = Node('int_4368', parent=DeclarationSpecifiers4421924368)
Identifier4421924048 = Node('Identifier_4048', parent=Declaration4421924432)
leaf = Node('arg1_4048', parent=Identifier4421924048)
leaf = Node("Type Qualifier=['const'], Type=['int'], TokenLocation=(9, 116, 20)", parent=Identifier4421924048)
Declaration4421924688 = Node('Declaration_4688', parent=PassUpNode4421924816)
DeclarationSpecifiers4421924624 = Node('DeclarationSpecifiers_4624', parent=Declaration4421924688)
leaf = Node('char_4624', parent=DeclarationSpecifiers4421924624)
Identifier4421924560 = Node('Identifier_4560', parent=Declaration4421924688)
leaf = Node('arg2_4560', parent=Identifier4421924560)
leaf = Node("Type=['char'], TokenLocation=(9, 127, 31)", parent=Identifier4421924560)
CompoundStatement4421924240 = Node('CompoundStatement_4240', parent=FunctionDefintion4421924880)
DeclList4421925072 = Node('DeclList_5072', parent=CompoundStatement4421924240)
Declaration4421925136 = Node('Declaration_5136', parent=DeclList4421925072)
DeclarationSpecifiers4421924944 = Node('DeclarationSpecifiers_4944', parent=Declaration4421925136)
leaf = Node('int_4944', parent=DeclarationSpecifiers4421924944)
InitDeclList4421925008 = Node('InitDeclList_5008', parent=Declaration4421925136)
Identifier4421924752 = Node('Identifier_4752', parent=InitDeclList4421925008)
leaf = Node('var2_4752', parent=Identifier4421924752)
leaf = Node("Type=['int'], TokenLocation=(10, 140, 7)", parent=Identifier4421924752)
PassUpNode4421926352 = Node('StatementList*_6352', parent=CompoundStatement4421924240)
PassUpNode4421926416 = Node('StatementList*_6416', parent=PassUpNode4421926352)
AssignmentExpression4421925520 = Node('AssignmentExpression_5520', parent=PassUpNode4421926416)
PrimaryExpression4421925264 = Node('PrimaryExpression_5264', parent=AssignmentExpression4421925520)
Identifier4421925200 = Node('Identifier_5200', parent=PrimaryExpression4421925264)
leaf = Node('var2_5200', parent=Identifier4421925200)
leaf = Node("Type=['int'], TokenLocation=(10, 140, 7)", parent=Identifier4421925200)
BinOp4421925712 = Node('BinOp_5712', parent=AssignmentExpression4421925520)
PrimaryExpression4421925456 = Node('PrimaryExpression_5456', parent=BinOp4421925712)
Identifier4421925328 = Node('Identifier_5328', parent=PrimaryExpression4421925456)
leaf = Node('arg1_5328', parent=Identifier4421925328)
leaf = Node("Type Qualifier=['const'], Type=['int'], TokenLocation=(9, 116, 20)", parent=Identifier4421925328)
leaf = Node('+_5712', parent=BinOp4421925712)
PrimaryExpression4421925584 = Node('PrimaryExpression_5584', parent=BinOp4421925712)
Constant4421925392 = Node('Constant_5392', parent=PrimaryExpression4421925584)
leaf = Node('3_5392', parent=Constant4421925392)
leaf = Node('int _5712', parent=BinOp4421925712)
FunctionCall4421926032 = Node('FunctionCall_6032', parent=PassUpNode4421926416)
PrimaryExpression4421925904 = Node('PrimaryExpression_5904', parent=FunctionCall4421926032)
Identifier4421925648 = Node('Identifier_5648', parent=PrimaryExpression4421925904)
leaf = Node('fun1_5648', parent=Identifier4421925648)
leaf = Node("Return Type=['int'], Subtype='Function Prototype', Label='fun1', Arguments=[{'Type': ['int']}, {'Type': ['char']}], TokenLocation=(6, 56, 5)", parent=Identifier4421925648)
PassUpNode4421926288 = Node('ArgumentExpressionList*_6288', parent=FunctionCall4421926032)
PrimaryExpression4421925968 = Node('PrimaryExpression_5968', parent=PassUpNode4421926288)
Identifier4421925840 = Node('Identifier_5840', parent=PrimaryExpression4421925968)
leaf = Node('var2_5840', parent=Identifier4421925840)
leaf = Node("Type=['int'], TokenLocation=(10, 140, 7)", parent=Identifier4421925840)
PrimaryExpression4421926160 = Node('PrimaryExpression_6160', parent=PassUpNode4421926288)
Identifier4421926096 = Node('Identifier_6096', parent=PrimaryExpression4421926160)
leaf = Node('var1_6096', parent=Identifier4421926096)
leaf = Node("Type=['char'], TokenLocation=(2, 15, 6)", parent=Identifier4421926096)
IterationStatement4422025744 = Node('IterationStatement_5744', parent=PassUpNode4421926352)
AssignmentExpression4421926608 = Node('AssignmentExpression_6608', parent=IterationStatement4422025744)
PrimaryExpression4421926480 = Node('PrimaryExpression_6480', parent=AssignmentExpression4421926608)
Identifier4421925776 = Node('Identifier_5776', parent=PrimaryExpression4421926480)
leaf = Node('var2_5776', parent=Identifier4421925776)
leaf = Node("Type=['int'], TokenLocation=(10, 140, 7)", parent=Identifier4421925776)
PrimaryExpression4421926672 = Node('PrimaryExpression_6672', parent=AssignmentExpression4421926608)
Constant4421926544 = Node('Constant_6544', parent=PrimaryExpression4421926672)
leaf = Node('0_6544', parent=Constant4421926544)
BinOp4422025552 = Node('BinOp_5552', parent=IterationStatement4422025744)
PrimaryExpression4421926864 = Node('PrimaryExpression_6864', parent=BinOp4422025552)
Identifier4421926800 = Node('Identifier_6800', parent=PrimaryExpression4421926864)
leaf = Node('var2_6800', parent=Identifier4421926800)
leaf = Node("Type=['int'], TokenLocation=(10, 140, 7)", parent=Identifier4421926800)
leaf = Node('<_5552', parent=BinOp4422025552)
PrimaryExpression4422025424 = Node('PrimaryExpression_5424', parent=BinOp4422025552)
Constant4422025360 = Node('Constant_5360', parent=PrimaryExpression4422025424)
leaf = Node('10_5360', parent=Constant4422025360)
leaf = Node('int _5552', parent=BinOp4422025552)
PrimaryExpression4422025616 = Node('PrimaryExpression_5616', parent=IterationStatement4422025744)
Identifier4422025296 = Node('Identifier_5296', parent=PrimaryExpression4422025616)
leaf = Node('var2_5296', parent=Identifier4422025296)
leaf = Node("Type=['int'], TokenLocation=(10, 140, 7)", parent=Identifier4422025296)
CompoundStatement4422025680 = Node('CompoundStatement_5680', parent=IterationStatement4422025744)
DeclList4422026960 = Node('DeclList_6960', parent=CompoundStatement4422025680)
DeclList4422026384 = Node('DeclList_6384', parent=DeclList4422026960)
DeclList4422026064 = Node('DeclList_6064', parent=DeclList4422026384)
Declaration4422026128 = Node('Declaration_6128', parent=DeclList4422026064)
DeclarationSpecifiers4422025936 = Node('DeclarationSpecifiers_5936', parent=Declaration4422026128)
leaf = Node('int_5936', parent=DeclarationSpecifiers4422025936)
InitDeclList4422026000 = Node('InitDeclList_6000', parent=Declaration4422026128)
Identifier4422025872 = Node('Identifier_5872', parent=InitDeclList4422026000)
leaf = Node('var5_5872', parent=Identifier4422025872)
leaf = Node("Type=['int'], TokenLocation=(15, 230, 9)", parent=Identifier4422025872)
Declaration4422026448 = Node('Declaration_6448', parent=DeclList4422026384)
DeclarationSpecifiers4422026256 = Node('DeclarationSpecifiers_6256', parent=Declaration4422026448)
leaf = Node('float_6256', parent=DeclarationSpecifiers4422026256)
InitDeclList4422026320 = Node('InitDeclList_6320', parent=Declaration4422026448)
Identifier4422026192 = Node('Identifier_6192', parent=InitDeclList4422026320)
leaf = Node('var10_6192', parent=Identifier4422026192)
leaf = Node("Type=['float'], TokenLocation=(16, 246, 11)", parent=Identifier4422026192)
Declaration4422026832 = Node('Declaration_6832', parent=DeclList4422026960)
DeclarationSpecifiers4422026576 = Node('DeclarationSpecifiers_6576', parent=Declaration4422026832)
leaf = Node('int_6576', parent=DeclarationSpecifiers4422026576)
InitDeclList4422026704 = Node('InitDeclList_6704', parent=Declaration4422026832)
ArrayDeclaration4422026896 = Node('ArrayDeclaration_6896', parent=InitDeclList4422026704)
Identifier4422026512 = Node('Identifier_6512', parent=ArrayDeclaration4422026896)
leaf = Node('arr1_6512', parent=Identifier4422026512)
leaf = Node("Array Size=['10'], Subtype='Array', Type=['int'], TokenLocation=(17, 261, 9)", parent=Identifier4422026512)
PrimaryExpression4422026768 = Node('PrimaryExpression_6768', parent=ArrayDeclaration4422026896)
Constant4422026640 = Node('Constant_6640', parent=PrimaryExpression4422026768)
leaf = Node('10_6640', parent=Constant4422026640)
CompoundStatement4422027024 = Node('CompoundStatement_7024', parent=CompoundStatement4422025680)
DeclList4422027344 = Node('DeclList_7344', parent=CompoundStatement4422027024)
Declaration4422027408 = Node('Declaration_7408', parent=DeclList4422027344)
DeclarationSpecifiers4422027216 = Node('DeclarationSpecifiers_7216', parent=Declaration4422027408)
leaf = Node('char_7216', parent=DeclarationSpecifiers4422027216)
InitDeclList4422027280 = Node('InitDeclList_7280', parent=Declaration4422027408)
Identifier4422027152 = Node('Identifier_7152', parent=InitDeclList4422027280)
leaf = Node('var7_7152', parent=Identifier4422027152)
leaf = Node("Type=['char'], TokenLocation=(19, 288, 12)", parent=Identifier4422027152)
FunctionDefintion4422027984 = Node('FunctionDefintion_7984', parent=PassUpNode4422067792)
DeclarationSpecifiers4421926736 = Node('DeclarationSpecifiers_6736', parent=FunctionDefintion4422027984)
leaf = Node('int_6736', parent=DeclarationSpecifiers4421926736)
FunctionPrototype4422027472 = Node('FunctionPrototype_7472', parent=FunctionDefintion4422027984)
Identifier4422027536 = Node('Identifier_7536', parent=FunctionPrototype4422027472)
leaf = Node('fun1_7536', parent=Identifier4422027536)
leaf = Node("Return Type=['int'], Subtype='Function Prototype', Label='fun1', Arguments=[{'Type': ['int']}, {'Type': ['char']}], TokenLocation=(6, 56, 5)", parent=Identifier4422027536)
PassUpNode4422027920 = Node('ParameterList*_7920', parent=FunctionPrototype4422027472)
Declaration4422027088 = Node('Declaration_7088', parent=PassUpNode4422027920)
DeclarationSpecifiers4422027600 = Node('DeclarationSpecifiers_7600', parent=Declaration4422027088)
leaf = Node('int_7600', parent=DeclarationSpecifiers4422027600)
Identifier4422025488 = Node('Identifier_5488', parent=Declaration4422027088)
leaf = Node('arg3_5488', parent=Identifier4422025488)
leaf = Node("Type=['int'], TokenLocation=(25, 323, 14)", parent=Identifier4422025488)
Declaration4422027792 = Node('Declaration_7792', parent=PassUpNode4422027920)
DeclarationSpecifiers4422027728 = Node('DeclarationSpecifiers_7728', parent=Declaration4422027792)
leaf = Node('char_7728', parent=DeclarationSpecifiers4422027728)
Identifier4422027664 = Node('Identifier_7664', parent=Declaration4422027792)
leaf = Node('arg4_7664', parent=Identifier4422027664)
leaf = Node("Type=['char'], TokenLocation=(25, 334, 25)", parent=Identifier4422027664)
CompoundStatement4422025808 = Node('CompoundStatement_5808', parent=FunctionDefintion4422027984)
DeclList4422066320 = Node('DeclList_6320', parent=CompoundStatement4422025808)
DeclList4422028816 = Node('DeclList_8816', parent=DeclList4422066320)
DeclList4422028496 = Node('DeclList_8496', parent=DeclList4422028816)
DeclList4422028176 = Node('DeclList_8176', parent=DeclList4422028496)
Declaration4422028240 = Node('Declaration_8240', parent=DeclList4422028176)
DeclarationSpecifiers4422028048 = Node('DeclarationSpecifiers_8048', parent=Declaration4422028240)
leaf = Node('int_8048', parent=DeclarationSpecifiers4422028048)
InitDeclList4422028112 = Node('InitDeclList_8112', parent=Declaration4422028240)
Identifier4422027856 = Node('Identifier_7856', parent=InitDeclList4422028112)
leaf = Node('var2_7856', parent=Identifier4422027856)
leaf = Node("Type=['int'], TokenLocation=(26, 349, 9)", parent=Identifier4422027856)
Declaration4422028560 = Node('Declaration_8560', parent=DeclList4422028496)
DeclarationSpecifiers4422028368 = Node('DeclarationSpecifiers_8368', parent=Declaration4422028560)
leaf = Node('char_8368', parent=DeclarationSpecifiers4422028368)
InitDeclList4422028432 = Node('InitDeclList_8432', parent=Declaration4422028560)
Identifier4422028304 = Node('Identifier_8304', parent=InitDeclList4422028432)
leaf = Node('var3_8304', parent=Identifier4422028304)
leaf = Node("Type=['char'], TokenLocation=(27, 364, 10)", parent=Identifier4422028304)
Declaration4422028880 = Node('Declaration_8880', parent=DeclList4422028816)
DeclarationSpecifiers4422028688 = Node('DeclarationSpecifiers_8688', parent=Declaration4422028880)
leaf = Node('float_8688', parent=DeclarationSpecifiers4422028688)
InitDeclList4422028752 = Node('InitDeclList_8752', parent=Declaration4422028880)
Identifier4422028624 = Node('Identifier_8624', parent=InitDeclList4422028752)
leaf = Node('var6_8624', parent=Identifier4422028624)
leaf = Node("Type=['float'], TokenLocation=(28, 380, 11)", parent=Identifier4422028624)
Declaration4422029264 = Node('Declaration_9264', parent=DeclList4422066320)
DeclarationSpecifiers4422029008 = Node('DeclarationSpecifiers_9008', parent=Declaration4422029264)
leaf = Node('int_9008', parent=DeclarationSpecifiers4422029008)
InitDeclList4422029136 = Node('InitDeclList_9136', parent=Declaration4422029264)
ArrayDeclaration4422066256 = Node('ArrayDeclaration_6256', parent=InitDeclList4422029136)
Identifier4422028944 = Node('Identifier_8944', parent=ArrayDeclaration4422066256)
leaf = Node('arr_8944', parent=Identifier4422028944)
leaf = Node("Array Size=['10'], Subtype='Array', Type=['int'], TokenLocation=(29, 394, 9)", parent=Identifier4422028944)
PrimaryExpression4422029200 = Node('PrimaryExpression_9200', parent=ArrayDeclaration4422066256)
Constant4422029072 = Node('Constant_9072', parent=PrimaryExpression4422029200)
leaf = Node('10_9072', parent=Constant4422029072)
PassUpNode4422067152 = Node('StatementList*_7152', parent=CompoundStatement4422025808)
AssignmentExpression4422066704 = Node('AssignmentExpression_6704', parent=PassUpNode4422067152)
PrimaryExpression4422066448 = Node('PrimaryExpression_6448', parent=AssignmentExpression4422066704)
Identifier4422066384 = Node('Identifier_6384', parent=PrimaryExpression4422066448)
leaf = Node('var2_6384', parent=Identifier4422066384)
leaf = Node("Type=['int'], TokenLocation=(26, 349, 9)", parent=Identifier4422066384)
CastNode4422066960 = Node('CastNode_6960', parent=AssignmentExpression4422066704)
leaf = Node('float _6960', parent=CastNode4422066960)
leaf = Node('int _6960', parent=CastNode4422066960)
BinOp4422066896 = Node('BinOp_6896', parent=CastNode4422066960)
PrimaryExpression4422066640 = Node('PrimaryExpression_6640', parent=BinOp4422066896)
Identifier4422066512 = Node('Identifier_6512', parent=PrimaryExpression4422066640)
leaf = Node('var6_6512', parent=Identifier4422066512)
leaf = Node("Type=['float'], TokenLocation=(28, 380, 11)", parent=Identifier4422066512)
leaf = Node('+_6896', parent=BinOp4422066896)
PrimaryExpression4422066768 = Node('PrimaryExpression_6768', parent=BinOp4422066896)
Constant4422066576 = Node('Constant_6576', parent=PrimaryExpression4422066768)
leaf = Node('4.0_6576', parent=Constant4422066576)
leaf = Node('float _6896', parent=BinOp4422066896)
SelectionStatement4422067600 = Node('SelectionStatement_7600', parent=PassUpNode4422067152)
BinOp4422067472 = Node('BinOp_7472', parent=SelectionStatement4422067600)
PrimaryExpression4422067088 = Node('PrimaryExpression_7088', parent=BinOp4422067472)
Identifier4422066832 = Node('Identifier_6832', parent=PrimaryExpression4422067088)
leaf = Node('var0_6832', parent=Identifier4422066832)
leaf = Node("Type=['int'], TokenLocation=(1, 4, 5)", parent=Identifier4422066832)
leaf = Node('<_7472', parent=BinOp4422067472)
CastNode4422067536 = Node('CastNode_7536', parent=BinOp4422067472)
leaf = Node('char _7536', parent=CastNode4422067536)
leaf = Node('int _7536', parent=CastNode4422067536)
PrimaryExpression4422067344 = Node('PrimaryExpression_7344', parent=CastNode4422067536)
Identifier4422067280 = Node('Identifier_7280', parent=PrimaryExpression4422067344)
leaf = Node('var1_7280', parent=Identifier4422067280)
leaf = Node("Type=['char'], TokenLocation=(2, 15, 6)", parent=Identifier4422067280)
leaf = Node('int _7472', parent=BinOp4422067472)
CompoundStatement4422067216 = Node('CompoundStatement_7216', parent=SelectionStatement4422067600)
FunctionCall4422067984 = Node('FunctionCall_7984', parent=CompoundStatement4422067216)
PrimaryExpression4422067728 = Node('PrimaryExpression_7728', parent=FunctionCall4422067984)
Identifier4422067664 = Node('Identifier_7664', parent=PrimaryExpression4422067728)
leaf = Node('fun1_7664', parent=Identifier4422067664)
leaf = Node("Return Type=['int'], Subtype='Function Prototype', Label='fun1', Arguments=[{'Type': ['int']}, {'Type': ['char']}], TokenLocation=(6, 56, 5)", parent=Identifier4422067664)
PassUpNode4422068240 = Node('ArgumentExpressionList*_8240', parent=FunctionCall4422067984)
PrimaryExpression4422067920 = Node('PrimaryExpression_7920', parent=PassUpNode4422068240)
Identifier4422067856 = Node('Identifier_7856', parent=PrimaryExpression4422067920)
leaf = Node('arg3_7856', parent=Identifier4422067856)
leaf = Node("Type=['int'], TokenLocation=(25, 323, 14)", parent=Identifier4422067856)
PrimaryExpression4422068112 = Node('PrimaryExpression_8112', parent=PassUpNode4422068240)
Identifier4422068048 = Node('Identifier_8048', parent=PrimaryExpression4422068112)
leaf = Node('arg4_8048', parent=Identifier4422068048)
leaf = Node("Type=['char'], TokenLocation=(25, 334, 25)", parent=Identifier4422068048)

for pre, fill, node in RenderTree(PassUpNode4422067792):
    if "TokenLocation" in node.name: print("%s%s" % (pre, node.name))
    else: print("%s%s" % (pre, node.name[:-5]) )

    
def f(node):
    if node.is_leaf and "TokenLocation" in node.name:
        return 'label="%s"' % (node.name)
    return 'label="%s"' % (node.name[:-5])

DotExporter(PassUpNode4422067792, nodeattrfunc=f).to_picture("AST.png")
        