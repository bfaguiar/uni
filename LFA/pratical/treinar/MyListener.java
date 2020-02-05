import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;
import java.util.*;

public class MyListener extends testeBaseListener {
	
	ParseTreeProperty<String> values = new ParseTreeProperty<>();
	Map<String, String> variables = new HashMap<>();

		@Override public void exitPrnt(testeParser.PrntContext ctx) { 
			System.out.println(values.get(ctx.operation()));
		}

		@Override public void exitDeclation(testeParser.DeclationContext ctx) {
			variables.put(ctx.VAR().getText(), values.get(ctx.operation()));
		 }

		@Override public void exitInput(testeParser.InputContext ctx) { 
			Scanner sc = new Scanner(System.in);
			System.out.print(values.get(ctx.operation()));
			values.put(ctx, sc.hasNextLine() ? sc.nextLine() : ""); // if sc has next line do "sc.NextLine()", else do " "" "
		}

		@Override public void exitSubs(testeParser.SubsContext ctx) { 
			values.put(ctx, values.get(ctx.operation(0)).replace(values.get(ctx.operation(1)), values.get(ctx.operation(2))));
		}


		@Override public void exitConcat(testeParser.ConcatContext ctx) {
			values.put(ctx, values.get(ctx.operation(0)) + values.get(ctx.operation(1))); 
		}
		

		@Override public void exitString(testeParser.StringContext ctx) {
			values.put(ctx, ctx.STRING().getText().replace("\"", ""));
		}

		@Override public void exitVar(testeParser.VarContext ctx) {
			System.out.println(ctx.VAR().getText());
			values.put(ctx, variables.get(ctx.VAR().getText()));
		}
}