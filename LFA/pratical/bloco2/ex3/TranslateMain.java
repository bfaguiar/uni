import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;
import java.util.*;
import java.io.*;

import static java.lang.System.*;

public class TranslateMain {
   public static void main(String[] args) throws Exception {

      // create a CharStream that reads from standard input: //  CharStream input = CharStreams.fromStream(System.in);

      CharStream input = null;

      try {

        input = CharStreams.fromStream(new FileInputStream(new File("numbers.txt")));

      } catch (FileNotFoundException e) {

        err.println("ERROR: reading number file!");
        System.exit(1);

      }

      // create a lexer that feeds off of input CharStream:
      TranslateLexer lexer = new TranslateLexer(input);
      // create a buffer of tokens pulled from the lexer:
      CommonTokenStream tokens = new CommonTokenStream(lexer);
      // create a parser that feeds off the tokens buffer:
      TranslateParser parser = new TranslateParser(tokens);
      // replace error listener:
      //parser.removeErrorListeners(); // remove ConsoleErrorListener
      //parser.addErrorListener(new ErrorHandlingListener());

      // begin parsing at file rule:

      ParseTree tree = parser.file();

      if (parser.getNumberOfSyntaxErrors() == 0) {

         // print LISP-style tree:
         // System.out.println(tree.toStringTree(parser));
         ParseTreeWalker walker = new ParseTreeWalker();
         ConstructNumberMappings mappings = new ConstructNumberMappings();
         walker.walk(mappings, tree);

      }

   }

}
