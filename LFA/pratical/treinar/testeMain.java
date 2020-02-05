import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;
import java.io.*;

public class testeMain {
   public static void main(String[] args) throws Exception {
      // create a CharStream that reads from standard input:

      InputStream stream = new FileInputStream(new File(args[0]));
      CharStream input = CharStreams.fromStream(stream);
      // create a lexer that feeds off of input CharStream:
      testeLexer lexer = new testeLexer(input);
      // create a buffer of tokens pulled from the lexer:
      CommonTokenStream tokens = new CommonTokenStream(lexer);
      // create a parser that feeds off the tokens buffer:
      testeParser parser = new testeParser(tokens);
      // replace error listener:
      //parser.removeErrorListeners(); // remove ConsoleErrorListener
      //parser.addErrorListener(new ErrorHandlingListener());
      // begin parsing at file rule:
      ParseTree tree = parser.file();
      if (parser.getNumberOfSyntaxErrors() == 0) {
         MyListener listener1 = new MyListener();
         ParseTreeWalker walker = new ParseTreeWalker();
         walker.walk(listener1, tree);
         // print LISP-style tree:
         // System.out.println(tree.toStringTree(parser));
      }
   }
}
