// Generated from teste.g by ANTLR 4.7.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link testeParser}.
 */
public interface testeListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link testeParser#file}.
	 * @param ctx the parse tree
	 */
	void enterFile(testeParser.FileContext ctx);
	/**
	 * Exit a parse tree produced by {@link testeParser#file}.
	 * @param ctx the parse tree
	 */
	void exitFile(testeParser.FileContext ctx);
	/**
	 * Enter a parse tree produced by the {@code print}
	 * labeled alternative in {@link testeParser#inst}.
	 * @param ctx the parse tree
	 */
	void enterPrint(testeParser.PrintContext ctx);
	/**
	 * Exit a parse tree produced by the {@code print}
	 * labeled alternative in {@link testeParser#inst}.
	 * @param ctx the parse tree
	 */
	void exitPrint(testeParser.PrintContext ctx);
	/**
	 * Enter a parse tree produced by the {@code declaration}
	 * labeled alternative in {@link testeParser#inst}.
	 * @param ctx the parse tree
	 */
	void enterDeclaration(testeParser.DeclarationContext ctx);
	/**
	 * Exit a parse tree produced by the {@code declaration}
	 * labeled alternative in {@link testeParser#inst}.
	 * @param ctx the parse tree
	 */
	void exitDeclaration(testeParser.DeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link testeParser#prnt}.
	 * @param ctx the parse tree
	 */
	void enterPrnt(testeParser.PrntContext ctx);
	/**
	 * Exit a parse tree produced by {@link testeParser#prnt}.
	 * @param ctx the parse tree
	 */
	void exitPrnt(testeParser.PrntContext ctx);
	/**
	 * Enter a parse tree produced by {@link testeParser#declation}.
	 * @param ctx the parse tree
	 */
	void enterDeclation(testeParser.DeclationContext ctx);
	/**
	 * Exit a parse tree produced by {@link testeParser#declation}.
	 * @param ctx the parse tree
	 */
	void exitDeclation(testeParser.DeclationContext ctx);
	/**
	 * Enter a parse tree produced by the {@code input}
	 * labeled alternative in {@link testeParser#operation}.
	 * @param ctx the parse tree
	 */
	void enterInput(testeParser.InputContext ctx);
	/**
	 * Exit a parse tree produced by the {@code input}
	 * labeled alternative in {@link testeParser#operation}.
	 * @param ctx the parse tree
	 */
	void exitInput(testeParser.InputContext ctx);
	/**
	 * Enter a parse tree produced by the {@code string}
	 * labeled alternative in {@link testeParser#operation}.
	 * @param ctx the parse tree
	 */
	void enterString(testeParser.StringContext ctx);
	/**
	 * Exit a parse tree produced by the {@code string}
	 * labeled alternative in {@link testeParser#operation}.
	 * @param ctx the parse tree
	 */
	void exitString(testeParser.StringContext ctx);
	/**
	 * Enter a parse tree produced by the {@code subs}
	 * labeled alternative in {@link testeParser#operation}.
	 * @param ctx the parse tree
	 */
	void enterSubs(testeParser.SubsContext ctx);
	/**
	 * Exit a parse tree produced by the {@code subs}
	 * labeled alternative in {@link testeParser#operation}.
	 * @param ctx the parse tree
	 */
	void exitSubs(testeParser.SubsContext ctx);
	/**
	 * Enter a parse tree produced by the {@code var}
	 * labeled alternative in {@link testeParser#operation}.
	 * @param ctx the parse tree
	 */
	void enterVar(testeParser.VarContext ctx);
	/**
	 * Exit a parse tree produced by the {@code var}
	 * labeled alternative in {@link testeParser#operation}.
	 * @param ctx the parse tree
	 */
	void exitVar(testeParser.VarContext ctx);
	/**
	 * Enter a parse tree produced by the {@code concat}
	 * labeled alternative in {@link testeParser#operation}.
	 * @param ctx the parse tree
	 */
	void enterConcat(testeParser.ConcatContext ctx);
	/**
	 * Exit a parse tree produced by the {@code concat}
	 * labeled alternative in {@link testeParser#operation}.
	 * @param ctx the parse tree
	 */
	void exitConcat(testeParser.ConcatContext ctx);
}