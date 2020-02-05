// Generated from teste.g by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class testeParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, STRING=8, VAR=9, 
		WS=10;
	public static final int
		RULE_file = 0, RULE_inst = 1, RULE_prnt = 2, RULE_declation = 3, RULE_operation = 4;
	public static final String[] ruleNames = {
		"file", "inst", "prnt", "declation", "operation"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'print'", "':'", "'+'", "'input'", "'('", "')'", "'/'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, null, null, "STRING", "VAR", "WS"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "teste.g"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public testeParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class FileContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(testeParser.EOF, 0); }
		public List<InstContext> inst() {
			return getRuleContexts(InstContext.class);
		}
		public InstContext inst(int i) {
			return getRuleContext(InstContext.class,i);
		}
		public FileContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_file; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof testeListener ) ((testeListener)listener).enterFile(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof testeListener ) ((testeListener)listener).exitFile(this);
		}
	}

	public final FileContext file() throws RecognitionException {
		FileContext _localctx = new FileContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_file);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(13);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__0 || _la==VAR) {
				{
				{
				setState(10);
				inst();
				}
				}
				setState(15);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(16);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InstContext extends ParserRuleContext {
		public InstContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_inst; }
	 
		public InstContext() { }
		public void copyFrom(InstContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class PrintContext extends InstContext {
		public PrntContext prnt() {
			return getRuleContext(PrntContext.class,0);
		}
		public PrintContext(InstContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof testeListener ) ((testeListener)listener).enterPrint(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof testeListener ) ((testeListener)listener).exitPrint(this);
		}
	}
	public static class DeclarationContext extends InstContext {
		public DeclationContext declation() {
			return getRuleContext(DeclationContext.class,0);
		}
		public DeclarationContext(InstContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof testeListener ) ((testeListener)listener).enterDeclaration(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof testeListener ) ((testeListener)listener).exitDeclaration(this);
		}
	}

	public final InstContext inst() throws RecognitionException {
		InstContext _localctx = new InstContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_inst);
		try {
			setState(20);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				_localctx = new PrintContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(18);
				prnt();
				}
				break;
			case VAR:
				_localctx = new DeclarationContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(19);
				declation();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PrntContext extends ParserRuleContext {
		public OperationContext operation() {
			return getRuleContext(OperationContext.class,0);
		}
		public PrntContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prnt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof testeListener ) ((testeListener)listener).enterPrnt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof testeListener ) ((testeListener)listener).exitPrnt(this);
		}
	}

	public final PrntContext prnt() throws RecognitionException {
		PrntContext _localctx = new PrntContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_prnt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(22);
			match(T__0);
			setState(23);
			operation(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DeclationContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(testeParser.VAR, 0); }
		public OperationContext operation() {
			return getRuleContext(OperationContext.class,0);
		}
		public DeclationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declation; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof testeListener ) ((testeListener)listener).enterDeclation(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof testeListener ) ((testeListener)listener).exitDeclation(this);
		}
	}

	public final DeclationContext declation() throws RecognitionException {
		DeclationContext _localctx = new DeclationContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_declation);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(25);
			match(VAR);
			setState(26);
			match(T__1);
			setState(27);
			operation(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class OperationContext extends ParserRuleContext {
		public OperationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operation; }
	 
		public OperationContext() { }
		public void copyFrom(OperationContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class InputContext extends OperationContext {
		public OperationContext operation() {
			return getRuleContext(OperationContext.class,0);
		}
		public InputContext(OperationContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof testeListener ) ((testeListener)listener).enterInput(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof testeListener ) ((testeListener)listener).exitInput(this);
		}
	}
	public static class StringContext extends OperationContext {
		public TerminalNode STRING() { return getToken(testeParser.STRING, 0); }
		public StringContext(OperationContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof testeListener ) ((testeListener)listener).enterString(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof testeListener ) ((testeListener)listener).exitString(this);
		}
	}
	public static class SubsContext extends OperationContext {
		public List<OperationContext> operation() {
			return getRuleContexts(OperationContext.class);
		}
		public OperationContext operation(int i) {
			return getRuleContext(OperationContext.class,i);
		}
		public SubsContext(OperationContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof testeListener ) ((testeListener)listener).enterSubs(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof testeListener ) ((testeListener)listener).exitSubs(this);
		}
	}
	public static class VarContext extends OperationContext {
		public TerminalNode VAR() { return getToken(testeParser.VAR, 0); }
		public VarContext(OperationContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof testeListener ) ((testeListener)listener).enterVar(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof testeListener ) ((testeListener)listener).exitVar(this);
		}
	}
	public static class ConcatContext extends OperationContext {
		public List<OperationContext> operation() {
			return getRuleContexts(OperationContext.class);
		}
		public OperationContext operation(int i) {
			return getRuleContext(OperationContext.class,i);
		}
		public ConcatContext(OperationContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof testeListener ) ((testeListener)listener).enterConcat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof testeListener ) ((testeListener)listener).exitConcat(this);
		}
	}

	public final OperationContext operation() throws RecognitionException {
		return operation(0);
	}

	private OperationContext operation(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		OperationContext _localctx = new OperationContext(_ctx, _parentState);
		OperationContext _prevctx = _localctx;
		int _startState = 8;
		enterRecursionRule(_localctx, 8, RULE_operation, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(45);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__3:
				{
				_localctx = new InputContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(30);
				match(T__3);
				setState(31);
				match(T__4);
				setState(32);
				operation(0);
				setState(33);
				match(T__5);
				}
				break;
			case T__4:
				{
				_localctx = new SubsContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(35);
				match(T__4);
				setState(36);
				operation(0);
				setState(37);
				match(T__6);
				setState(38);
				operation(0);
				setState(39);
				match(T__6);
				setState(40);
				operation(0);
				setState(41);
				match(T__5);
				}
				break;
			case STRING:
				{
				_localctx = new StringContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(43);
				match(STRING);
				}
				break;
			case VAR:
				{
				_localctx = new VarContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(44);
				match(VAR);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(52);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ConcatContext(new OperationContext(_parentctx, _parentState));
					pushNewRecursionContext(_localctx, _startState, RULE_operation);
					setState(47);
					if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
					setState(48);
					match(T__2);
					setState(49);
					operation(6);
					}
					} 
				}
				setState(54);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 4:
			return operation_sempred((OperationContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean operation_sempred(OperationContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 5);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f:\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\7\2\16\n\2\f\2\16\2\21\13\2\3\2\3\2\3\3"+
		"\3\3\5\3\27\n\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3"+
		"\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\60\n\6\3\6\3\6\3\6\7\6\65\n"+
		"\6\f\6\16\68\13\6\3\6\2\3\n\7\2\4\6\b\n\2\2\2:\2\17\3\2\2\2\4\26\3\2\2"+
		"\2\6\30\3\2\2\2\b\33\3\2\2\2\n/\3\2\2\2\f\16\5\4\3\2\r\f\3\2\2\2\16\21"+
		"\3\2\2\2\17\r\3\2\2\2\17\20\3\2\2\2\20\22\3\2\2\2\21\17\3\2\2\2\22\23"+
		"\7\2\2\3\23\3\3\2\2\2\24\27\5\6\4\2\25\27\5\b\5\2\26\24\3\2\2\2\26\25"+
		"\3\2\2\2\27\5\3\2\2\2\30\31\7\3\2\2\31\32\5\n\6\2\32\7\3\2\2\2\33\34\7"+
		"\13\2\2\34\35\7\4\2\2\35\36\5\n\6\2\36\t\3\2\2\2\37 \b\6\1\2 !\7\6\2\2"+
		"!\"\7\7\2\2\"#\5\n\6\2#$\7\b\2\2$\60\3\2\2\2%&\7\7\2\2&\'\5\n\6\2\'(\7"+
		"\t\2\2()\5\n\6\2)*\7\t\2\2*+\5\n\6\2+,\7\b\2\2,\60\3\2\2\2-\60\7\n\2\2"+
		".\60\7\13\2\2/\37\3\2\2\2/%\3\2\2\2/-\3\2\2\2/.\3\2\2\2\60\66\3\2\2\2"+
		"\61\62\f\7\2\2\62\63\7\5\2\2\63\65\5\n\6\b\64\61\3\2\2\2\658\3\2\2\2\66"+
		"\64\3\2\2\2\66\67\3\2\2\2\67\13\3\2\2\28\66\3\2\2\2\6\17\26/\66";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}