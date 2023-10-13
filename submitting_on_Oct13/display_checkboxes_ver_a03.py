"""

conda activate P10A


ver=a03


# Setting up a server:
hug -f ./display_checkboxes_ver_${ver}.py

# Web browser access:
http://localhost:8000/test_module



"""

import hug
import pandas as pd



@hug.get('/test_module', output = hug.output_format.html)
def test_module():
    #score_file_path = "./niraj_san_report_score_URLs.csv"
    #frame = pd.read_csv(score_file_path, sep = ",")
    #urls = frame["URL"].tolist()
    #urls = urls[:7]
    sample_urls = [
            "https://indigodata.co.jp", 
            "https://blendata.co", 
            "https://pig-data.jp/", 
            "https://www.itconsul.co.jp", 
            "https://www.passionned.nl", 
            "https://www.shtockdata.com", 
            "https://www.zdh.co.jp", 
            ]
    urls = sample_urls

    header = """
<html>
    <p>
        <font size="5">
            <strong>Testing Module Loaded.</strong>
        </font>
    </p>

    <fieldset>
        <legend>Select URL(s):</legend>
        <form action="/submit_my_response" method="post">
    """
    def get_record(i):
        text = f"""
            <div>
                <input 
                    type="checkbox" 
                    id="selected_urls_id" 
                    name="selected_urls" 
                    value="{urls[i]}"
                    />
                <label for="url_{i}">
                    <a href="{urls[i]}" target="_blank">
                        {urls[i]}
                    </a>
                </label>
            </div>
        """
        return text
    body = "\n".join([get_record(i) for i in range(len(urls))])
    
    # Example body:
    """
        <div>
            <input type="checkbox" id="scales" name="scales" checked />
            <label for="scales">Scales</label>
        </div>
        <div>
            <input type="checkbox" id="horns" name="horns" />
            <label for="horns">Horns</label>
        </div>

    """
    footer = """
            <div>
                <button type="submit">Submit</button>
            </div>
        </form>
    </fieldset>

</html>
    """

    return header + body + footer




@hug.post('/submit_my_response', output = hug.output_format.html)
def internal_func(selected_urls = []):
    header = """
<html>
    <p>
        <font size="5">
            <strong>Post Method Loaded.</strong>
        </font>
    </p>
    """
    
    def add_record(i):
        text = f"""
            <div>
                <label for="url_{i}">
                    <a href="{selected_urls[i]}" target="_blank">
                        {selected_urls[i]}
                    </a>
                </label>
            </div>
        """
        return text
    body = "\n".join([add_record(i) for i in range(len(selected_urls))])
    

    footer = """
</html>
    """
    return header + body + footer