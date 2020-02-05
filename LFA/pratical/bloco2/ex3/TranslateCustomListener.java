import java.util.*;

class TranslateCustomListener extends TranslateBaseListener {

  protected Map<String, Integer> mappings = new HashMap<>();

  public boolean exists(String key) {

    assert key != null;
    return mappings.containsKey(key);

  }

  public Integer value(String key) {

    assert key != null;
    assert exists(key);
    return mappings.get(key);

  }
  @Override
  public void exitLine(TranslateParser.LineContext ctx) {

    String key = ctx.CARACT().getText();
    Integer value = Integer.parseInt(ctx.NUM().getText());

    if(exists(key)) {
      System.err.println("ERROR: Repeated key.");
      System.exit(1);
    }

    mappings.put(key, value);

  }

}
