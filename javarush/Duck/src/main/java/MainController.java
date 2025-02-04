@Controller //указывает фреймворку SpringBoot, что этот класс будет использоваться для обслуживания входящих веб-запросов.
public class MainController {

    @GetMapping("/")
    public String viewIndexPage(Model model) {
        model.addAttribute("header", "Maven Generate War");
        return "index";
    }
}