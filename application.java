public class Application extends io.dropwizard.Application<MyConfiguration> {
    public static void main(String[] args) throws Exception {
        new Application().run(args);
    }

    @Override
    public void run(MyConfiguration configuration, Environment environment) {
        // Setup REST endpoints and other configurations
    }
}
