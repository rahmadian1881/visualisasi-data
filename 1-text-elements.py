# import library yang dibutuhkan
import streamlit as st

# Bagian 1 : text element
# header - untuk membuat tulisan header
#st.header("Praktikum 1 Visualisasi Data") # membuat header
# st.subheader("Bagian 1: Text Element") # untuk membuat sub judul yang lebih kecil
# st.text("Ini Text biasa tanpa format") # untuk membuat teks polos tanpa format
# st.markdown("**Tria Maulida Sari** - *0110222300*") # markdown untuk memformat teks tebal/miring
# st.caption("ini caption") # teks kecil dibawah elemen (untuk penjelasan)

# Bagian 2 : Menampilkan Rumus (LaTex)
# st.header("Displaying laTex")

# ========================================== 

st.title("**Anggota Kelompok:**")
st.write("**1. Tria Maulida Sari - 0110222300**")
st.write("**2. Alma Nur Fajriah - 0110222222**")
st.write("**3. Rahma Dian Nurhikma - 0110222082**")

st.title('Tugas Praktikum 1')
st.write('Tugas Praktikum 1 - Visualisasi Data')
st.header("ini header")
st.subheader("Ini subheader")
st.caption("ini caption")

#Displaying plain text
st.text("Hi, \nWorld\t!")
st.text('Selamat Datang')
st.text('Streamlit')

#Displaying Markdown
st.markdown("**Hi, World**")

# DISPLAYING LaTex
st.latex(r'''cos2\theta = 1 - 2sin^2\theta''')
st.latex("""(a+b)^2 = a^2 + b^2 + 2ab""")
st.latex(r'''\frac{\partial u}{\partial t}
         = h^2 \left( \frac{\partial^2 u}{\partial x^2}
         + \frac{\partial^2 u}{\partial y^2}
         + \frac{\partial^2 u}{\partial z^2} \right)''')

# DISPLAYING PYTHON CODE
st.subheader("""Python Code""")
code = '''def hello():
print("Hello, TriaMaul!")'''
st.code(code, language='python')

# DISPLAYING JAVA CODE
st.subheader("""Java Code""")
st.code("""public class CFG {
        public static void main(String args[])
        {
        System.out.println("Hello Tria!");
        }
        }""", language='javascript')
st.subheader("""Javascript Code""")
st.code(""" <p od="demo"></p>
        <script>
        try {
        addlert("Welcome guest!");
        }
        catch(err) {
        document.getElementById("demo").innerHTML = err.message;
        }
        </script> """)
