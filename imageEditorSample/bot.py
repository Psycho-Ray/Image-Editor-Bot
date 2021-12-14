from botcity.web import WebBot


class Bot(WebBot):
    # Convenient refactoring to keep the code clean
    def quick_find(self, label, *, threshold=None, matching=0.9, waiting_time=10000, best=True, grayscale=False):
        if not self.find(label, threshold=threshold, matching=matching, waiting_time=waiting_time, best=best,
                         grayscale=grayscale):
            raise ValueError("Resource not found")

    def action(self, execution=None):
        # Configure whether or not to run on headless mode
        self.headless = False

        # Uncomment to set the WebDriver path
        self.driver_path = "./chromedriver.exe"

        # Opens the Pixlr website
        self.browse("https://pixlr.com/e/")

        # Skip random propaganda
        if self.find("skip"):
            self.click()

        # Opens a new URL
        self.quick_find("loadURL")
        self.click()
        self.paste("https://www.distrelec.biz/Web/WebShopImages/landscape_large/2-/01/30110722-01.jpg")

        # Confirms
        self.quick_find("loadButton")
        self.click()

        # Applies the Invert Filter
        self.quick_find("adjustment")
        self.click()
        self.quick_find("invert")
        self.click()

        # Applies the Gaussian Blur Filter
        self.quick_find("filter")
        self.click()
        self.quick_find("details")
        self.move()
        self.quick_find("gaussianBlur")
        self.click()
        self.quick_find("amount")
        self.click_relative(350, 0)
        self.control_a()
        self.paste("7")
        self.quick_find("apply")
        self.click()

        # Applies the Find Edges filter
        self.quick_find("filter")
        self.click()
        self.quick_find("findEdges")
        self.click()

        # Applies the Threshold Filter
        self.quick_find("adjustment")
        self.click()
        self.quick_find("invert")
        self.click()

        # Save File
        self.quick_find("file")
        self.click()
        self.quick_find("export")
        self.click()
        self.quick_find("export_image")
        self.click()
        self.enter(1000)

        # Stop the browser and clean up
        self.stop_browser()


if __name__ == '__main__':
    Bot.main()
