// Generated from Translate.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link TranslateParser}.
 */
public interface TranslateListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link TranslateParser#file}.
	 * @param ctx the parse tree
	 */
	void enterFile(TranslateParser.FileContext ctx);
	/**
	 * Exit a parse tree produced by {@link TranslateParser#file}.
	 * @param ctx the parse tree
	 */
	void exitFile(TranslateParser.FileContext ctx);
	/**
	 * Enter a parse tree produced by {@link TranslateParser#line}.
	 * @param ctx the parse tree
	 */
	void enterLine(TranslateParser.LineContext ctx);
	/**
	 * Exit a parse tree produced by {@link TranslateParser#line}.
	 * @param ctx the parse tree
	 */
	void exitLine(TranslateParser.LineContext ctx);
}