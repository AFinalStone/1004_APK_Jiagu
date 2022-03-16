class JavaPlugin(object):

    @staticmethod
    def run_jar_main(jar_file_name, args):
        cmd = f"java -jar {jar_file_name} args"

    @staticmethod
    def run_jar(jar_file_name, java_class):
        cmd = f"java -cp {jar_file_name} {java_class}args"

    @staticmethod
    def make_class(jar):
        cmd = "javac "
