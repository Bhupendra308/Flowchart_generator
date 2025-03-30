# def generate_html_with_mermaid(mermaid_code):
#     html_template = f"""
#     <!DOCTYPE html>
#     <html lang="en">
#     <head>
#         <meta charset="UTF-8">
#         <meta name="viewport" content="width=device-width, initial-scale=1.0">
#         <title>Mermaid Example</title>
#         <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
#         <style>
#             body {{
#                 font-family: Arial, sans-serif;
#                 background: linear-gradient(to right, #f9d423, #ff4e50); /* Gradient background */
#                 margin: 0;
#                 padding: 0;
#                 display: flex;
#                 justify-content: center;
#                 align-items: center;
#                 height: 100vh;
#             }}
#             .container {{
#                 background-color: #ffffff;
#                 padding: 30px;
#                 box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
#                 border-radius: 12px;
#                 text-align: center;
#                 width: 80vw;
#                 height: 80vh;
#                 display: flex;
#                 justify-content: center;
#                 align-items: center;
#                 border: 1px solid #0097a7;
#             }}
#             .mermaid {{
#                 text-align: center;
#                 width: 100%;
#                 height: 100%;
#             }}
#             .mermaid svg {{
#                 width: 100%;
#                 height: 100%;
#             }}
#             h1 {{
#                 color: #00796b; /* Custom title color */
#                 margin-bottom: 20px;
#             }}
#             /* Custom CSS for links */
#             .mermaid a {{
#                 text-decoration: none;  /* Remove underline */
#                 color: inherit;         /* Inherit the natural text color */
#                 transition: transform 0.3s; /* Smooth transition for transform */
#             }}
#             .mermaid a:hover {{
#                 color: #00796b;         /* Change color on hover */
#                 text-decoration: underline; /* Add underline on hover */
#                 transform: scale(1.1);  /* Scale up the text size on hover */
#             }}
#         </style>
#     </head>
#     <body>
#         <div class="container">
#             <div class="mermaid">
#                 {mermaid_code}
#             </div>
#         </div>
#         <script type="module">
#             import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
#             mermaid.initialize({{ startOnLoad: true, themeCSS: `
#                 .node rect, .node circle {{
#                     stroke-width: 24px;
#                 }}
#                 .node text {{
#                     font-size: 18px;
#                 }}
#                 svg {{
#                     font-size: 22px;
#                 }}
#             ` }});
#         </script>
#     </body>
#     </html>
#     """
#     return html_template


# def generate_html_with_mermaid(mermaid_code):
#     html_template = f"""
#     <!DOCTYPE html>
#     <html lang="en">
#     <head>
#         <meta charset="UTF-8">
#         <meta name="viewport" content="width=device-width, initial-scale=1.0">
#         <title>Mermaid Example</title>
#         <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
#         <script src="https://cdn.jsdelivr.net/npm/html2canvas@1.4.1/dist/html2canvas.min.js"></script>
#         <style>
#             body {{
#                  font-family: Arial, sans-serif;
#                  background: linear-gradient(to right, #f9d423, #ff4e50); /* Gradient background */
#                  margin: 0;
#                  padding: 0;
#                  display: flex;

#                 justify-content: center;
#                  align-items: center;
#                  height: 100vh;
#              }}
#              .container {{
#                  background-color: #ffffff;
#                  padding: 30px;
#                  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
#                  border-radius: 12px;
#                  text-align: center;
#                  width: 80vw;
#                  height: 80vh;
#                  display: flex;
#                  justify-content: center;
#                  align-items: center;
#                  border: 1px solid #0097a7;
#              }}
#              .mermaid {{
#                  text-align: center;
#                  width: 100%;
#                  height: 100%;
#              }}
#              .mermaid svg {{
#                  width: 100%;
#                  height: 100%;
#              }}
#              h1 {{
#                  color: #00796b; /* Custom title color */
#                  margin-bottom: 20px;
#              }}
#              /* Custom CSS for links */
#              .mermaid a {{
#                  text-decoration: none;  /* Remove underline */
#                  color: inherit;         /* Inherit the natural text color */
#                  transition: transform 0.3s; /* Smooth transition for transform */
#              }}
#              .mermaid a:hover {{
#                  color: #00796b;         /* Change color on hover */
#                  text-decoration: underline; /* Add underline on hover */
#                  transform: scale(1.1);  /* Scale up the text size on hover */
#              }}
#             button {{
#                 background-color: #00796b;
#                 color: white;
#                 padding: 10px 20px;
#                 border: none;
#                 border-radius: 5px;
#                 cursor: pointer;
#                 font-size: 16px;
#                 margin-top: 10px;
#             }}
#             button:hover {{
#                 background-color: #005f54;
#             }}
#         </style>
#     </head>
#     <body>
#         <div class="container" id="mermaid-container">
#             <div class="mermaid">
#                 {mermaid_code}
#             </div>
#         </div>
#         <button id="download-btn">Download Screenshot</button>
#         <script type="module">
#             import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
#             mermaid.initialize({{ startOnLoad: true, themeCSS: `
#                 .node rect, .node circle {{
#                     stroke-width: 24px;
#                 }}
#                 .node text {{
#                     font-size: 18px;
#                 }}
#                 svg {{
#                     font-size: 22px;
#                 }}
#             ` }});

#             // Function to save screenshot
#         document.getElementById('download-btn').addEventListener('click', () => {{
#             const container = document.getElementById('mermaid-container');
#             html2canvas(container, {{ scale: 2 }}).then((canvas) => {{
#                 // Convert the canvas to a downloadable image
#                 const image = canvas.toDataURL("image/png");
#                 const link = document.createElement("a");
#                 link.href = image;
#                 link.download = "mermaid_diagram.png";
#                 link.click();
#             }});
#         }});
#         </script>
#     </body>
#     </html>
#     """
#     return html_template

def generate_html_with_mermaid(mermaid_code):
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mermaid Example</title>
        <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/html2canvas@1.4.1/dist/html2canvas.min.js"></script>
        <style>
            body {{
                 font-family: Arial, sans-serif;
                 background: rgba(20, 20, 20, 0.8);
                 margin: 0;
                 padding: 0;
                 display: flex;
                 justify-content: center;
                 align-items: center;
                 height: 100vh;
             }}
             .container {{
                 background-color: #ffffff;
                 padding: 30px;
                 box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                 border-radius: 12px;
                 text-align: center;
                 width: 80vw;
                 height: 80vh;
                 display: flex;
                 justify-content: center;
                 align-items: center;
                 border: 1px solid #0097a7;
             }}
             .mermaid {{
                 text-align: center;
                 width: 100%;
                 height: 100%;
             }}
             .mermaid svg {{
                 width: 100%;
                 height: 100%;
             }}
             h1 {{
                 color: #00796b; /* Custom title color */
                 margin-bottom: 20px;
             }}
             /* Custom CSS for links */
             .mermaid a {{
                 text-decoration: none;  /* Remove underline */
                 color: inherit;         /* Inherit the natural text color */
                 transition: transform 0.3s; /* Smooth transition for transform */
             }}
             .mermaid a:hover {{
                 color: #00796b;         /* Change color on hover */
                 text-decoration: underline; /* Add underline on hover */
                 transform: scale(1.1);  /* Scale up the text size on hover */
             }}
            button {{
                background-color: #00796b;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
                margin-top: 10px;
            }}
            button:hover {{
                background-color: #005f54;
            }}
        </style>
    </head>
    <body>
        <div class="container" id="mermaid-container">
            <div class="mermaid">
                {mermaid_code}
            </div>
        </div>
        <button id="download-btn">Download Screenshot</button>
        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{ startOnLoad: true, themeCSS: `
                .node rect, .node circle {{
                    stroke-width: 24px;
                }}
                .node text {{
                    font-size: 18px;
                }}
                svg {{
                    font-size: 22px;
                }}
            ` }});

            // Function to save screenshot
        document.getElementById('download-btn').addEventListener('click', () => {{
            const container = document.getElementById('mermaid-container');
            html2canvas(container, {{ scale: 2 }}).then((canvas) => {{
                // Convert the canvas to a downloadable image
                const image = canvas.toDataURL("image/png");
                const link = document.createElement("a");
                link.href = image;
                link.download = "mermaid_diagram.png";
                link.click();
            }});
        }});
        </script>
    </body>
    </html>
    """
    return html_template
