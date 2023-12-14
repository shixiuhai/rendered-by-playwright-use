# 获取网页请求js
import requests

url = "http://127.0.0.1:9001/rendered_by_playwright/requests"

payload = {
    "url": "https://item.taobao.com/item.htm?spm=a21bo.jianhua.201876.1.5af92a89EP5tnC&id=36903311829&scm=1007.40986.276750.0&pvid=24189f20-0708-421d-980f-730cd37cfc05",
    "return_type": "screenshot",
    "is_block_image": False,
    "browser_type": "chromium",
    "timeout": 15,
    "js_script_after_page":"""
   function getSliderElement() {
    
    return document.evaluate('//*[@id="nc_1_n1z"]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
}
async function simulateMouseMovement(startX, startY, distances) {
    const sliderElement = getSliderElement();

    for (let i = 0; i < distances.length; i++) {
        const distance = distances[i];

        startX += distance;

        sliderElement.dispatchEvent(
            new MouseEvent('mousemove', { clientX: startX, clientY: startY, bubbles: true, cancelable: true, composed: true })
        );
        console.log("滑动一次" + (i + 1));

        await new Promise(resolve => setTimeout(resolve, 600)); // Adding a 2-second delay
    }
}

async function moveSlider() {
    const sliderElement = getSliderElement();
    const sliderRect = sliderElement.getBoundingClientRect();
    const startX = 0;
    const startY = 0;
    console.log("开始滑动坐标" + startX)
    console.log("结束滑动坐标" + startY)

    const ratios = [1,3,2,1,4,5,2]; // 请根据实际情况调整


    const totalDistance = 310;
    const distances = ratios.map(ratio => (ratio / ratios.reduce((a, b) => a + b, 0)) * totalDistance);
    console.log(distances)
    


    sliderElement.dispatchEvent(new MouseEvent('mousedown', { bubbles: true, cancelable: true, composed: true })); // 按下鼠标左键
    await simulateMouseMovement(startX, startY, distances);
    sliderElement.dispatchEvent(new MouseEvent('mouseup', { bubbles: true, cancelable: true, composed: true })); // 放下鼠标左键
}



await moveSlider();

    
    """,
    "cookies": [
        {
            "domain": ".taobao.com",
            "name": "cna",
            "path": "/",
            "value": "11vzHZqQkVgCASe6tKSHLPTd"
        },
        {
            "domain": ".taobao.com",
            "name": "_tb_token_",
            "path": "/",
            "value": "35515518b3feb"
        }
    ]
}
headers = {"content-type": "application/json"}

response = requests.request("POST", url, json=payload, headers=headers)

with open("page.png","wb") as f:
    f.write(response.content)