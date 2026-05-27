import streamlit as st
import random as rd
st.success("All the best for the quiz")
gk= [
    {
        "question": "Which planet is known as the Red Planet'?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars",
        "img":"https://imgs.search.brave.com/zy6kyxhfMc6mqLdL6f-0BUG_oIiUus9RWnl8WeUQEa4/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvNDkw/MzQzODQ4L3Bob3Rv/L3N1bnJpc2UtaW4t/bWFycy5qcGc_cz02/MTJ4NjEyJnc9MCZr/PTIwJmM9Mno2aEdV/UlVUNHdETnlWV2VP/eFNBLWhmVFM0TXZu/Mk9ld3EtX1R1eWtU/az0"},
    {
        "question": "What is the official currency of Japan?",
        "options": ["Won", "Yuan", "Yen", "Baht"],
        "answer": "Yen",
        "img":"https://imgs.search.brave.com/hcp05uA-V2kqVmIEg6U56dioIjqd1FHOHv3EKMBKJ6I/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvaW1z/aXMwMjAtMDM0L3Bo/b3RvL3llbi5qcGc_/cz02MTJ4NjEyJnc9/MCZrPTIwJmM9bnN4/eXA2NWlsczZXbnpE/ZHQ2SkRYMzlOY0Za/bGYwMlN6TlU5dmt1/MnozVT0"
    },
    {
        "question": "Which country is home to the most islands in the world?",
        "options": ["Indonesia", "Philippines", "Sweden", "Canada"],
        "answer": "Sweden",
        "img":"https://imgs.search.brave.com/9mi8f6krqD3W2K7ppBcO8q7y3A9SBwNEqV0duY5jbvE/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9pLmlu/c2lkZXIuY29tLzVk/MzYxNmUyOGQ2NjQy/NWUxZjFmODE1ND93/aWR0aD03MDA"
    },
    {
        "question": "Who directed the 2009 sci-fi blockbuster 'Avatar'?",
        "options": ["Steven Spielberg", "Christopher Nolan", "James Cameron", "Peter Jackson"],
        "answer": "James Cameron",
        "img":"https://imgs.search.brave.com/4YUfhKTHLgGWAf4gQOtEplGazS93dMFx7cMQ538rhT8/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMjI1/MDE5NzIxNy9waG90/by9ib3Vsb2duZS1i/aWxsYW5jb3VydC1m/cmFuY2UtamFtZXMt/Y2FtZXJvbi1hdHRl/bmRzLXRoZS1hdmF0/YXItZmlyZS1hbmQt/YXNoLWV1cm9wZWFu/LXByZW1pZXJlLmpw/Zz9zPTYxMng2MTIm/dz0wJms9MjAmYz1Z/VGYxSjB4VXRGZkpU/bHJrcE9OVmlVMVJp/MFZLWVZwblFicmJm/Ukx0NkRJPQ"
    },
    {
        "question": "What is the smallest fully independent country in the world?",
        "options": ["Monaco", "Vatican City", "San Marino", "Liechtenstein"],
        "answer": "Vatican City",
        "img":"https://imgs.search.brave.com/ACDsP4W64vU5hf4dD2Qg9nuGV82otBZrZS66ug4z_6I/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMjAw/MzUzOTUwOS9waG90/by9waWF6emEtZGVs/LXBvcG9sby1vbi1h/LXN1bm55LWRheS1h/ZXJpYWwtdmlldy1y/b21lLWl0YWx5Lmpw/Zz9zPTYxMng2MTIm/dz0wJms9MjAmYz1m/T0lkdGpXX0d3XzVM/M19kV3BCOEJSX0NX/YXV2YUFFUmdvUzhC/SG9UNnJ3PQ"
    },
    {
        "question": "Which desert is the largest non-polar desert in the world?",
        "options": ["Gobi Desert", "Kalahari Desert", "Sahara Desert", "Arabian Desert"],
        "answer": "Sahara Desert",
        "img":"https://imgs.search.brave.com/Au-N5XPEeae9cCQbN9U4Fw9NT0zT-iKryDED9taIf7w/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTU1/MTU3NDczL3Bob3Rv/L3RvdXJpc3RzLW9u/LXRyYWluLW9mLWNh/bWVscy1pbi1zYWhh/cmEtbGVkLWJ5LWd1/aWRlLmpwZz9zPTYx/Mng2MTImdz0wJms9/MjAmYz1vU29PVzFI/RVN4X3VqdkgxTlM5/U0hIS09CSHNsODBI/M3lvczZqYTd6Q0pZ/PQ"
    },
    {
        "question": "Who painted 'The Starry Night'?",
        "options": ["Pablo Picasso", "Claude Monet", "Vincent Van Gogh", "Salvador Dali"],
        "answer": "Vincent Van Gogh",
        "img":"https://imgs.search.brave.com/maJF1DmBeLFRqlTYFqpdaRWTTq6V3IhP7FEsNy9YJ7E/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9pMC53/cC5jb20vYmxvZy5h/cnRzcGVyLmNvbS93/cC1jb250ZW50L3Vw/bG9hZHMvMjAxOS8w/NC90YWJsZWF1LWxh/LW51aXQtZXRvaWxl/ZS12aW5jZW50LXZh/bi1nb2doLTc1LXgt/NTUtYy0xLmpwZz9m/aXQ9MTIwMCw2NzUm/c3NsPTE"
    },
    {
        "question": "In which city would you find the headquarters of the United Nations?",
        "options": ["Geneva", "New York City", "Paris", "London"],
        "answer": "New York City",
        "img":"https://imgs.search.brave.com/sPptNZUeoaXeQ32LJLeXWati8mf0PDQ2NOJM0e-K7eU/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTQy/MDAyNjM5Mi9waG90/by93aGl0ZS1ob3Vz/ZS13aXRoLWNyb3dk/LWluLWZyb250Lmpw/Zz9zPTYxMng2MTIm/dz0wJms9MjAmYz10/YTlwQUFhMUlkN0JG/YWVrUzAxM2l6c1A1/dDNwd3NWWElJVTZR/VHBFeEE4PQ"
    },
    {
        "question": "What is the longest river in the world ?",
        "options": ["Nile", "Amazon", "Yangtze", "Mississippi"],
        "answer": "Nile",
        "img":"https://imgs.search.brave.com/3D2MU03mRU9-JkEi9SqHU8gj1wND4c50xxxe7MZJtvM/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9zdGF0/aWMudmVjdGVlenku/Y29tL3N5c3RlbS9y/ZXNvdXJjZXMvdGh1/bWJuYWlscy8wMTcv/NTIxLzA5OC9zbWFs/bC9iYW5rcy1vZi10/aGUtbmlsZS1yaXZl/ci1pbi1lZ3lwdC1w/aG90by5qcGc"
    },
    {
        "question": "Which continent is known as the 'Dark Continent'?",
        "options": ["Asia", "South America", "Africa", "Antarctica"],
        "answer": "Africa",
        "img":"https://imgs.search.brave.com/VYLvmF2sPWujDriSdImF4ZXw6XIf4zNwRIta4GYegy8/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly93d3cu/Y2JjLmNhL2tpZHNu/ZXdzL2ltYWdlcy9p/U2hvd1NwZWVkLWFy/dGljbGUtRXN3YXRp/bmkucG5n"
    }
]

science= [
    {
        "question": "What is the hardest known natural substance on Earth?",
        "options": ["Graphene", "Diamond", "Quartz", "Titanium"],
        "answer": "Diamond",
        "img":"https://imgs.search.brave.com/ioopfkRaIrnuzoWKiMXu7KdNN2LFdw1s4jfHsfrcg3A/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMjE1/MDIwNjQ1OC9waG90/by9oeWRyb2dlbi1w/ZXJpb2RpYy10YWJs/ZS1lbGVtZW50LW1p/bmluZy1zY2llbmNl/LW5hdHVyZS1pbm5v/dmF0aW9uLWNoZW1p/Y2FsLWVsZW1lbnRz/LXVzZWQtaW4uanBn/P2I9MSZzPTYxMng2/MTImdz0wJms9MjAm/Yz1tTXJYajdILTYt/UEdYVldNUFlDT0RV/RmFacE5RUExYYlpj/Ui1YekFZbGxZPQ"
    },
    {
        "question": "Which chemical element has the symbol 'Au'?",
        "options": ["Silver", "Aluminum", "Gold", "Argon"],
        "answer": "Gold",
        "img":"https://imgs.search.brave.com/2Y7YstW-eBZ70B2HVAQtHkTu_MuvKrkhvPYDy8sWBQk/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly90My5m/dGNkbi5uZXQvanBn/LzAxLzMyLzY0Lzkw/LzM2MF9GXzEzMjY0/OTA5NF9icVJKSGVQ/TWh2VWVLMlVaN0Jm/WG9lcjlNWnlUZjFv/Ni5qcGc"
    },
    {
        "question": "Which scientist is credited with formulating the Uncertainty Principle in quantum mechanics?",
        "options": ["Albert Einstein", "Niels Bohr", "Erwin Schrödinger", "Werner Heisenberg"],
        "answer": "Werner Heisenberg",
        "img":"https://imgs.search.brave.com/XU5IkIUsVKWqH9SiQvWRMHANJk0GJBvXBQjsuDUwcmM/rs:fit:0:180:1:0/g:ce/aHR0cHM6Ly9zdGF0/aWMud2lraWEubm9j/b29raWUubmV0L2Jy/ZWFraW5nYmFkL2lt/YWdlcy80LzQzL1Nl/YXNvbl8yX3Byb21v/X3BpY180LmpwZy9y/ZXZpc2lvbi9sYXRl/c3Qvc2NhbGUtdG8t/d2lkdGgtZG93bi8x/ODA_Y2I9MjAxMjA2/MTcyMTIyNTY"},
    {
        "question": "Which planet in our solar system has the most moons?",
        "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
        "answer": "Saturn",
        "img":"https://imgs.search.brave.com/2LKuTX0MC9IHEHr_qdGNo4YL9RGRlSnE9APB_Z_rVoA/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9pbWFn/ZXMudW5zcGxhc2gu/Y29tL3Bob3RvLTE3/MDE0ODY0ODUzNzQt/NDQzN2RjMmMxYzFk/P2ZtPWpwZyZxPTYw/Jnc9MzAwMCZhdXRv/PWZvcm1hdCZmaXQ9/Y3JvcCZpeGxpYj1y/Yi00LjEuMCZpeGlk/PU0zd3hNakEzZkRC/OE1IeHpaV0Z5WTJo/OE4zeDhjMkYwZFhK/dWZHVnVmREI4ZkRC/OGZId3c"
    },
    {
        "question": "What is the scientific term for the study of fossils?",
        "options": ["Archaeology", "Anthropology", "Paleontology", "Geology"],
        "answer": "Paleontology",
        "img":"https://imgs.search.brave.com/RomGiSbY0KyIMv0zq6z1S2i0AsC6o7hi23I-gyfRGdg/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvOTg4/NDEyMTcwL3Bob3Rv/L2UtanBnLmpwZz9z/PTYxMng2MTImdz0w/Jms9MjAmYz1NRU5M/VTNaYTR2c3VUbF95/RlZjZ0NLeTc5cVBE/UXBheGotTFViNWlk/cVNvPQ"
    },
    {
        "question": "At what temperature are Celsius and Fahrenheit equal?",
        "options": ["-40 degrees", "0 degrees", "32 degrees", "-273 degrees"],
        "answer": "-40 degrees",
        "img":"https://imgs.search.brave.com/5Hx_DVIzCwFZ236PDR69OTKFpeyICNbO2lrBKAXOhTQ/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9pbWcu/ZnJlZXBpay5jb20v/cHJlbWl1bS12ZWN0/b3IvY29sZC13YXJt/LXRoZXJtb21ldGVy/LXRlbXBlcmF0dXJl/LXdlYXRoZXItdGhl/cm1vbWV0ZXJzLWNl/bHNpdXMtZmFocmVu/aGVpdC1tZXRlb3Jv/bG9neS1zY2FsZS10/ZW1wLWNvbnRyb2wt/ZGV2aWNlLWljb25f/MTc2NDExLTU1My5q/cGc_c2VtdD1haXNf/c2VfZW5yaWNoZWQm/dz03NDAmcT04MA"
    },
    {
        "question": "Which subatomic particle has a negative electric charge?",
        "options": ["Proton", "Neutron", "Electron", "Photon"],
        "answer": "Electron",
        "img":"https://imgs.search.brave.com/k1FCRKjRAZgoZxOHrjUC_aoVACOUlq23YfiDTkbQ8oo/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTYw/MzgwNjU3L3Bob3Rv/L2F0b20uanBnP3M9/NjEyeDYxMiZ3PTAm/az0yMCZjPTRZcGlC/aFdaWWtlR09aVWVD/a3F4VGNaWmphV2RF/RGRJY0lzaG1Dd1Z5/ZTA9"
    },
    {
        "question": "What vitamin deficiency is the primary cause of scurvy?",
        "options": ["Vitamin A", "Vitamin B12", "Vitamin C", "Vitamin D"],
        "answer": "Vitamin C",
        "img":"https://imgs.search.brave.com/Etc7nUHeHkeF81yLkY-nBPsdlYp1H71aovvYCY-oS1E/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly90aHVt/YnMuZHJlYW1zdGlt/ZS5jb20vYi92aXRh/bWluLWMtY2l0cnVz/LXNlbGVjdGl2ZS1m/b2N1cy1mb29kLTM4/Mjk0NDQwNC5qcGc"
    },
    {
        "question": "What is the most abundant gas in the Earth's atmosphere?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "answer": "Nitrogen",
        "img":"https://imgs.search.brave.com/3QMEtzq3N_wdv9eHoF9F3DzYAG1AX5AxlAufbB4Hm84/rs:fit:0:180:1:0/g:ce/aHR0cHM6Ly93d3cu/dGhvdWdodGNvLmNv/bS90aG1iL3kyeU92/OFZlS3ctSVNBOXUy/Sk5LRFFibTVkRT0v/MjUweDAvZmlsdGVy/czpub191cHNjYWxl/KCk6bWF4X2J5dGVz/KDE1MDAwMCk6c3Ry/aXBfaWNjKCkvR2V0/dHlJbWFnZXMtMTAz/Mjc2OTU2MC1mZWU3/NTQ1ODFlMDE0MWI0/YjZhZGNjY2M1NGM4/YTA2ZC5qcGc"
    },
    {
        "question": "How many bones are in the adult human body?",
        "options": ["206", "212", "198", "256"],
        "answer": "206",
        "img":"https://imgs.search.brave.com/oOfbD7Bqxij-mk9f5Mm3Hnw0x59MjOJaj7Lutqi0Yv8/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9pbWcu/ZnJlZXBpay5jb20v/cHJlbWl1bS1waG90/by9iaWctc2tlbGV0/b24tZmxleGluZy1o/aXMtbXVzY2xlcy13/aXRoLWNvbWljLWZs/YWlyXzUxMDk1OC0x/NDQzLmpwZw"
    }
]

history= [
    {
        "question": "In which year did the French Revolution begin?",
        "options": ["1776", "1789", "1812", "1848"],
        "answer": "1789",
        "img":"https://imgs.search.brave.com/awpuL3EUyAo7E5a6uH5cI8mPC7tj2jSRqdCyfMdFhzk/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly93YWxs/cGFwZXJhY2Nlc3Mu/Y29tL2Z1bGwvMjQ3/MDI5My5qcGc"
    },
    {
        "question": "Who was the first Emperor of Rome?",
        "options": ["Julius Caesar", "Nero", "Augustus", "Marcus Aurelius"],
        "answer": "Augustus",
        "img":"https://imgs.search.brave.com/MvXwRWSleLAYj_quZUrwEvEggh4r0M4BvvImbiY4ico/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9yb21h/bi1lbXBpcmUubmV0/L3dwLWNvbnRlbnQv/dXBsb2Fkcy8yMDI1/LzAzL0p1bGl1cy1D/YWVzYXJzLUZhbWUt/YW5kLXRoZS1TZW5h/dGVzLVdyb25nLUFz/c3VtcHRpb25zLmpw/Zw"
    },
    {
        "question": "The ancient city of Machu Picchu is located in which modern-day country?",
        "options": ["Mexico", "Colombia", "Peru", "Chile"],
        "answer": "Peru",
        "img":"https://imgs.search.brave.com/3y4elNpT3I0TAuX5gTInJRcJrd_HR4m3Jhy7rFhCjGU/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly93YWxs/cGFwZXJjYXQuY29t/L3cvZnVsbC9kL2Mv/My82MzQ3NjItMTk2/MHgxMzA3LWRlc2t0/b3AtaGQtcGVydS13/YWxscGFwZXItaW1h/Z2UuanBn"
    },
    {
        "question": "Who was the first female Prime Minister of India?",
        "options": ["Sarojini Naidu", "Indira Gandhi", "Pratibha Patil", "Sushma Swaraj"],
        "answer": "Indira Gandhi",
        "img":"https://imgs.search.brave.com/VFLg9muHBRMVh7S7RahVRcUrnW5pB3lCwQoOMnUElSM/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9pLnBp/bmltZy5jb20vb3Jp/Z2luYWxzL2MwLzFl/LzFlL2MwMWUxZWY2/ZThhYThkNTJkNjc0/Yzk5YTY3MDIzZWI2/LmpwZw"
    },
    {
        "question": "In what year did World War II officially end?",
        "options": ["1943", "1944", "1945", "1946"],
        "answer": "1945",
        "img":"https://imgs.search.brave.com/VuwppK4eu3pFYaasayT-lMvsz5oXqhdlJwGl4SrZJc0/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9iZXJs/aW5leHBlcmllbmNl/cy5jb20vd3AtY29u/dGVudC91cGxvYWRz/LzIwMjUvMTEvYmVy/bGluZXhwZXJpZW5j/ZXNfbXl0aGJ1c3Rp/bmdiZXJsaW5fbmF6/aXNhbHV0ZV8xMS5q/cGc"
    },
    {
        "question": "Which Egyptian Pharaoh is famous for his intact tomb discovered in 1922?",
        "options": ["Ramses II", "Tutankhamun", "Khufu", "Akhenaten"],
        "answer": "Tutankhamun",
        "img":"https://imgs.search.brave.com/4pjn0baPITGNPz9Gtx-SEjEIuPBOccgNHx_ezF4E6TI/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly93MC5w/ZWFrcHguY29tL3dh/bGxwYXBlci83MTkv/NDM2L0hELXdhbGxw/YXBlci1lZ3lwdC1w/eXJhbWlkcy1kZXNl/cnQtY2l0eS1hbmQt/YmFja2dyb3VuZC1l/Z3lwdC04ay10aHVt/Ym5haWwuanBn"
    },
    {
        "question": "Who wrote the American Declaration of Independence?",
        "options": ["George Washington", "Alexander Hamilton", "Benjamin Franklin", "Thomas Jefferson"],
        "answer": "Thomas Jefferson",
        "img":"https://imgs.search.brave.com/8pQmHNCzm8DV4wxy1adDPCxV3FA0oQy-sdPfHAdhgLI/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9jZG4u/d2FsbHBhcGVyc2Fm/YXJpLmNvbS8yNy84/OC9YY3pCU1EuanBn"
    },
    {
        "question": "Which empire built the Colosseum in Rome?",
        "options": ["The Byzantine Empire", "The Ottoman Empire", "The Roman Empire", "The Holy Roman Empire"],
        "answer": "The Roman Empire",
        "img":"https://imgs.search.brave.com/RZ-8hnSC4J7iEm1IK1Q47f4Z98jX5BVD518rgRyVFeM/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly93YWxs/cGFwZXJhY2Nlc3Mu/Y29tL2Z1bGwvNjU4/MzA3LmpwZw"
    },
    {
        "question": "Who was known as the 'Iron Lady' of British politics?",
        "options": ["Queen Victoria", "Theresa May", "Margaret Thatcher", "Elizabeth I"],
        "answer": "Margaret Thatcher",
        "img":"https://imgs.search.brave.com/aqejxw0nWJN507-FGrBW0k9lAa0m6yrXYm56w6rGl5M/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9pbS5y/ZWRpZmYuY29tL25l/d3MvMjAxMy9hcHIv/MDhtYXJnYXJldDIw/LmpwZw"
    },
    {
        "question": "The Cold War was primarily a geopolitical tension between the USA and which other superpower?",
        "options": ["China", "The Soviet Union", "Germany", "Japan"],
        "answer": "The Soviet Union",
        "img":"https://imgs.search.brave.com/lVIP0xmv8IpjeCc1uS6R3Ile-6HAQOVfpW6R3_QFN38/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly93MC5w/ZWFrcHguY29tL3dh/bGxwYXBlci80NjQv/NDEyL0hELXdhbGxw/YXBlci1ob2xpZGF5/LWZsYWctd29ybGQt/d2FyLWlpLXZpY3Rv/cnktZGF5LTktbWF5/LXVzc3ItcmVpY2hz/dGFnLXRodW1ibmFp/bC5qcGc"
    }
]

sports= [
    {
        "question": "Which country has won the most FIFA World Cups in men's football?",
        "options": ["Germany", "Italy", "Argentina", "Brazil"],
        "answer": "Brazil",
        "img": "https://imgs.search.brave.com/BjTz-FXQumPOGGHMWwMp8EUKe2On0S4OhSmpwBgjioE/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly93YWxs/cGFwZXJzLmNvbS9p/bWFnZXMvdGh1bWJu/YWlsL2xpb25lbC1t/ZXNzaS1saWZ0aW5n/LXdvcmxkLWN1cC10/cm9waHktNDc5Z2p4/MnRrOHV6djN1dC53/ZWJw"   },
    {
        "question": "What is the exact length of a standard marathon?",
        "options": ["24.2 miles", "25.5 miles", "26.2 miles", "27.1 miles"],
        "answer": "26.2 miles",
        "img":"https://imgs.search.brave.com/_YUfFsKo5CtPecT01LDit21d8A-bMYvqLC0OXLxh1WE/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jYWxn/YXJ5bWFyYXRob24u/Y29tL3dwLWNvbnRl/bnQvdXBsb2Fkcy8y/MDI0LzEwLzIwMjQw/NTI2X0NBTEdBUllf/TUFSQVRIT05fTUFS/MDM5MkFCLTEtc2Nh/bGVkLmpwZw"
    },
    {
        "question": "Which sport is affectionately known as 'The Sweet Science'?",
        "options": ["Fencing", "Mixed Martial Arts", "Boxing", "Wrestling"],
        "answer": "Boxing",
        "img":"https://imgs.search.brave.com/nBWnHS0T_T4o8s755Anv8fA7hmB_xlRyEN19tNJ4_Mg/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvOTIz/MjM0NzUvcGhvdG8v/c291dGhwb3J0LWVu/Z2xhbmQtYm9keWJ1/aWxkZXJzLXBvc2Ut/Zm9yLWp1ZGdlcy1p/bi10aGUtdGhlLW1p/c3Rlci11bml2ZXJz/ZS1jb21wZXRpdGlv/bi1hdC10aGUuanBn/P3M9NjEyeDYxMiZ3/PTAmaz0yMCZjPWIw/UzFzX284QmtKbkxu/NXY1WmUxZ2JUMjdQ/LVhYZHVENXRnWXBm/TC14Mms9"
        
    },
    {
        "question": "How many players are on the court for a single basketball team during a game?",
        "options": ["4", "5", "6", "7"],
        "answer": "5",
        "img":"https://imgs.search.brave.com/-C5-91BMxey9TV_cZwicUIXEVbc_oZNIkQEhzpyIGoc/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTQ4/ODQ0ODAwMi9waG90/by93aWRlLXNob3Qt/cmVhci12aWV3LWNy/b3dkLWNoZWVyaW5n/LWR1cmluZy1wcm9m/ZXNzaW9uYWwtYmFz/ZWJhbGwtZ2FtZS5q/cGc_cz02MTJ4NjEy/Jnc9MCZrPTIwJmM9/NGFpLUdPWkZtbjQx/eUg0bjQ5YnE2ejln/VnhPV0Q0MmlJWlFT/cERuMVBXdz0"
    },
    {
        "question": "Which nation won the inaugural ICC Men's T20 World Cup in 2007?",
        "options": ["Australia", "Pakistan", "India", "West Indies"],
        "answer": "India",
        "img":"https://imgs.search.brave.com/ovfe234zNV34wC-a83PvC6wrVQmm-hFMfsWorpEQQ2g/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMjE5/MjIwNDQ5OS9waG90/by9zeWRuZXktYXVz/dHJhbGlhLXZpcmF0/LWtvaGxpLW9mLWlu/ZGlhLWxvb2tzLWRl/amVjdGVkLXdoaWxl/LWxlYXZpbmctdGhl/LWZpZWxkLWFmdGVy/LWJlaW5nLmpwZz9z/PTYxMng2MTImdz0w/Jms9MjAmYz0wUDNT/aWI0NmNReUNlWDJx/bm02NGRxdlhBbERC/d1d4ZDZsT3lGQ2ZO/OXFJPQ"
    },
    {
        "question": "Which Grand Slam tennis tournament is played on red clay courts?",
        "options": ["Australian Open", "Wimbledon", "US Open", "French Open"],
        "answer": "French Open",
        "img":"https://imgs.search.brave.com/lGD6A4wlv0L5w-H0L45naY9seqfBreHEZCTiZqFNF8E/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly93YWxs/cGFwZXJzLmNvbS9p/bWFnZXMvaGQvYXVz/dHJhbGlhbi1vcGVu/LXRlbm5pcy1hcmVu/YS12b2FweDZldmlo/cDJ2aG9iLmpwZw"},  
    {
        "question": "In standard cricket, what is the length of the pitch between the two sets of wickets?",
        "options": ["18 yards", "20 yards", "22 yards", "24 yards"],
        "answer": "22 yards",
        "img":"https://imgs.search.brave.com/9iZtSl0jpZRGZMTWp9HrrRPOTYHHjj0SS8vKBWMiDJw/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTE3/MTA4ODc4Ni9waG90/by9sZWVkcy1lbmds/YW5kLWJlbi1zdG9r/ZXMtb2YtZW5nbGFu/ZC1jZWxlYnJhdGVz/LWhpdHRpbmctdGhl/LXdpbm5pbmctcnVu/cy10by13aW4tdGhl/LTNyZC5qcGc_cz02/MTJ4NjEyJnc9MCZr/PTIwJmM9S0ZabXRX/dXhNRHJVOVI2Y3Uz/cVdaTmRZUk9kdlVl/NGdKbVB0M2FYQ0tw/cz0"
    },
    {
        "question": "Michael Phelps holds the record for the most Olympic gold medals. What is his sport?",
        "options": ["Gymnastics", "Track and Field", "Swimming", "Cycling"],
        "answer": "Swimming",
        "img":"https://imgs.search.brave.com/w8ZlkJ7GFDQKMoYmlSVVeWPVZLQjBRNBT0c-VPdRi0k/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9pLnBp/bmltZy5jb20vb3Jp/Z2luYWxzLzkwL2M1/L2M0LzkwYzVjNGY3/ODAwYTViMDM1MDEy/ZTJiNGNiNTA1YTNi/LmpwZw"
    },
    {
        "question": "Which country is credited with inventing table tennis?",
        "options": ["China", "Japan", "South Korea", "England"],
        "answer": "England",
        "img":"https://imgs.search.brave.com/-phCprcLAEmamm6XnNtbxKxz-Bdhc7QTEOWizA_gNkg/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9nY3At/bmEtaW1hZ2VzLmNv/bnRlbnRzdGFjay5j/b20vdjMvYXNzZXRz/L2JsdGVhNjA5Mzg1/OWFmNjE4M2IvYmx0/NDYxMWQxY2Y5MDA5/ZDg5MC82OTk4Y2M3/NTA3YTMwZGVjYWQ3/N2Q5ZDEvdGltb3Ro/ZWUtY2hhbGFtZXQt/bWFydHktc3VwcmVt/ZS5qcGc_YnJhbmNo/PXByb2R1Y3Rpb24m/d2lkdGg9Mzg0MCZx/dWFsaXR5PTc1JmF1/dG89d2VicCZjcm9w/PTM6Mg"
    },
    {
        "question": "In Formula 1 racing, what does a waved blue flag indicate to a driver?",
        "options": ["Danger ahead", "Session stopped", "Let a faster car pass", "Return to the pits"],
        "answer": "Let a faster car pass",
        "img":"https://imgs.search.brave.com/vSZmcgo9sJ2A6GtF5A1MYjT8uuwlmfN1ya0saK3hH60/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9pLnBp/bmltZy5jb20vb3Jp/Z2luYWxzL2UwL2Fi/L2RmL2UwYWJkZmQx/MzgxZDk2YmU1YzAy/NWQ3ZjVlMzVmNTcx/LmpwZw"
    }
]
  
color=[":red",":green",":blue",":yellow",":orange",":violet"]
st.sidebar.title("Welcome to the QUIZ app\nPlease provide neccesary information")
name=st.sidebar.text_input("Please enter your Name and tap ENTER")
if name:
    st.title(f"Welcome to the QUIZ app and Greetings to {rd.choice(color)}[{name}]")
category=st.sidebar.radio("Select the category of your choice",['General Knowledge','Science','History','Sports'],index=None)
if category:
    st.header(f"You have selected {rd.choice(color)}[{category}] category")
    st.write("""Following are the rules:
1) Question will be surfaced one after another
2) You have to select the correct option
3) Each question carries 10 points
4) No negative marking
5) To measure your responses click submit button at the very end
6) Your score will be displayed at the end of the quiz
""") 
st.sidebar.write("Designed and Engineered by")
st.sidebar.text("Shivam Joshi 💖")
dicts=[]
score=[]

def squiz(sports,dicts,score):
    count=1
    idx=0
    pr=10
    point=0
    with st.form(key=f"radio{count}"):
        for i in sports:
            st.header(f"Question {count} :\n\n\n\n{sports[idx]['question']}")  
            with col2:                    
                    st.image(sports[idx]["img"],width=1000)  
                    bar=st.progress(pr,text=f"Current Progress {pr}%") 
                    bar.progress(pr,text=f"Current Progress {pr}%")  
            ans0=st.radio(f"Following are the options for Question {count}:",sports[idx]["options"],index=None)
            if ans0==sports[idx]["answer"]:
                point+=10
                dicts.append(10)
                
                
            else:
                point=point
                dicts.append(0)
            idx+=1
            count+=1
            pr+=10
        sub=st.form_submit_button(f"Submit")
        for i in range(0,10):
            if i==10:
                break
            if i==0:
                score.append(dicts[i])
            else:
                extra=score[i-1]+dicts[i]
                score.append(extra) 
        if sub:
            results(score, dicts)
            st.balloons()
            st.snow()
            st.write(f"{point} are points")
            with col2:
                exp=st.expander("Click here to see the correct answers")
                for i in range(0,10):
                    exp.write(f"Question {i+1} : {sports[i]["answer"]}")
        st.success(f"Your score is {point} out of 100")
    st.markdown("---")     
    st.success("🎉 **Thank you for playing the Quiz!**")  
    left_tip, right_tip = st.columns(2)
        
    with left_tip:
        st.info("🔄 **Want to beat your high score?**\n\nSimply refresh the page to clear your answers and try again!")
            
    with right_tip:
        st.info("🎮 **Ready for a new challenge?**\n\nHead over to the sidebar to choose a completely different category!")
            
    st.write("Designed and Engineered by Shivam Joshi 💖")    
    st.audio("quiz.mp3",autoplay=True,loop=True,start_time=0)                      
    return score,dicts
def hquiz(history,dicts,score):
    count=1
    idx=0
    pr=10
    point=0
    with st.form(key=f"radio{count}"):
        for i in history:
            st.header(f"Question {count} :\n\n\n\n{history[idx]['question']}")  
            with col2:                    
                    st.image(history[idx]["img"],width=1000)  
                    bar=st.progress(pr,text=f"Current Progress {pr}%") 
                    bar.progress(pr,text=f"Current Progress {pr}%")  
            ans0=st.radio(f"Following are the options for Question {count}:",history[idx]["options"],index=None)
            if ans0==history[idx]["answer"]:
                point+=10
                dicts.append(10)
                
                
            else:
                point=point
                dicts.append(0)
            idx+=1
            count+=1
            pr+=10
        sub=st.form_submit_button(f"Submit")
        for i in range(0,10):
            if i==10:
                break
            if i==0:
                score.append(dicts[i])
            else:
                extra=score[i-1]+dicts[i]
                score.append(extra) 
        if sub:
            results(score, dicts)
            st.balloons()
            st.snow()
            st.write(f"{point} are points")    
            with col2:
                exp=st.expander("Click here to see the correct answers")
                for i in range(0,10):
                    exp.write(f"Question {i+1} : {history[i]["answer"]}")
        st.success(f"Your score is {point} out of 100")
    st.markdown("---")     
    st.success("🎉 **Thank you for playing the Quiz!**")        
       
    left_tip, right_tip = st.columns(2)
        
    with left_tip:
        st.info("🔄 **Want to beat your high score?**\n\nSimply refresh the page to clear your answers and try again!")
            
    with right_tip:
        st.info("🎮 **Ready for a new challenge?**\n\nHead over to the sidebar to choose a completely different category!")
            
    st.write("Designed and Engineered by Shivam Joshi 💖")
    st.audio("quiz.mp3",autoplay=True,loop=True,start_time=0)
    return score,dicts
def gquiz(gk,dicts,score):
    count=1
    idx=0
    pr=10
    point=0
    with st.form(key=f"radio{count}"):
        for i in gk:
            st.header(f"Question {count} :\n\n\n\n{gk[idx]['question']}")  
            with col2:                    
                    st.image(gk[idx]["img"],width=1000)  
                    bar=st.progress(pr,text=f"Current Progress {pr}%") 
                    bar.progress(pr,text=f"Current Progress {pr}%")  
            ans0=st.radio(f"Following are the options for Question {count}:",gk[idx]["options"],index=None)
            if ans0==gk[idx]["answer"]:
                point+=10
                dicts.append(10)
                
                
            else:
                point=point
                dicts.append(0)
            idx+=1
            count+=1
            pr+=10
        sub=st.form_submit_button(f"Submit")
        for i in range(0,10):
            if i==10:
                break
            if i==0:
                score.append(dicts[i])
            else:
                extra=score[i-1]+dicts[i]
                score.append(extra) 
        if sub:
            results(score, dicts)
            st.balloons()
            st.snow()
            st.write(f"{point} are points")
            with col2:
                exp=st.expander("Click here to see the correct answers")
                for i in range(0,10):
                    exp.write(f"Question {i+1} : {gk[i]["answer"]}")
                  
        st.success(f"Your score is {point} out of 100")   
    st.markdown("---")     
    st.success("🎉 **Thank you for playing the Quiz!**")
    
        
       
    left_tip, right_tip = st.columns(2)
        
    with left_tip:
        st.info("🔄 **Want to beat your high score?**\n\nSimply refresh the page to clear your answers and try again!")
            
    with right_tip:
        st.info("🎮 **Ready for a new challenge?**\n\nHead over to the sidebar to choose a completely different category!")
            
    st.write("Designed and Engineered by Shivam Joshi 💖")                           
    st.audio("quiz.mp3",autoplay=True,loop=True,start_time=0)
    return score,dicts
def scquiz(science,dicts,score):
    count=1
    idx=0
    pr=10
    point=0
    with st.form(key=f"radio{count}"):
        for i in science:
            st.header(f"Question {count} :\n\n\n\n{science[idx]['question']}")  
            with col2:                    
                    st.image(science[idx]["img"],width=1000)  
                    bar=st.progress(pr,text=f"Current Progress {pr}%") 
                    bar.progress(pr,text=f"Current Progress {pr}%")  
            ans0=st.radio(f"Following are the options for Question {count}:",science[idx]["options"],index=None)
            if ans0==science[idx]["answer"]:
                point+=10
                dicts.append(10)
                
                
            else:
                point=point
                dicts.append(0)
            idx+=1
            count+=1
            pr+=10
        sub=st.form_submit_button(f"Submit")
        for i in range(0,10):
            if i==10:
                break
            if i==0:
                score.append(dicts[i])
            else:
                extra=score[i-1]+dicts[i]
                score.append(extra) 
        if sub:
            results(score, dicts)
            st.balloons()
            st.snow()
            st.write(f"{point} are points")
            with col2:
                exp=st.expander("Click here to see the correct answers")
                for i in range(0,10):
                    exp.write(f"Question {i+1} : {science[i]["answer"]}")
    st.success(f"Your score is {point} out of 100")
    st.markdown("---")     
    st.success("🎉 **Thank you for playing the Quiz!**")
    
        
       
    left_tip, right_tip = st.columns(2)
        
    with left_tip:
        st.info("🔄 **Want to beat your high score?**\n\nSimply refresh the page to clear your answers and try again!")
            
    with right_tip:
        st.info("🎮 **Ready for a new challenge?**\n\nHead over to the sidebar to choose a completely different category!")
            
    st.write("Designed and Engineered by Shivam Joshi 💖")                                
    st.audio("quiz.mp3",autoplay=True,loop=True,start_time=0)
    return score,dicts
@st.dialog("Quiz Performance")  
def results(score, dicts):      
            col1,col2,col3,col4,col5=st.columns(5)
            with col1:
                st.metric(label="Question 1",value=score[0],delta=dicts[0])
            with col2:
                st.metric(label="Question 2",value=score[1],delta=dicts[1])
            with col3:  
                st.metric(label="Question 3",value=score[2],delta=dicts[2])
            with col4:
                st.metric(label="Question 4",value=score[3],delta=dicts[3])
            with col5:  
                st.metric(label="Question 5",value=score[4],delta=dicts[4])
            col6,col7,col8,col9,col10=st.columns(5)
            with col6:
                st.metric(label="Question 6",value=score[5],delta=dicts[5])
            with col7:  
                st.metric(label="Question 7",value=score[6],delta=dicts[6])
            with col8:  
                st.metric(label="Question 8",value=score[7],delta=dicts[7])
            with col9:
                st.metric(label="Question 9",value=score[8],delta=dicts[8])  
            with col10:
                st.metric(label="Question 10",value=score[9],delta=dicts[9])
            full=0
            for i in dicts:
                full+=i
            st.success(f"Your total score is {full} out of 100")      
        
col1,col2=st.columns([5,5.5])
with col1:           
    if category=="Sports":
        squiz(sports,dicts,score)
    elif category=="History":
        hquiz(history,dicts,score)
    elif category=="General Knowledge":  
        gquiz(gk,dicts,score)
    elif category=="Science":
        scquiz(science,dicts,score)      

        

