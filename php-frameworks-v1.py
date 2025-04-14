import streamlit as st

# Data: PHP frameworks categorized
frameworks = {
    "Full-Stack Frameworks": [
        "Laravel",
        "Symfony",
        "CodeIgniter",
        "CakePHP",
        "Yii",
        "Zend Framework (Laminas)",
        "Phalcon",
        "FuelPHP",
        "PHPixie",
        "Aura",
        "Agavi",
        "Prado",
        "Kohana (Discontinued)",
        "MODX Revolution",
        "Joomla! Framework",
        "Lithium",
        "QCubed (QCube)",
        "Flow",
        "FUSE"
    ],
    "Micro-Frameworks": [
        "Slim",
        "Lumen",
        "Fat-Free Framework (F3)",
        "Silex (Deprecated)",
        "Flight",
        "Pop PHP",
        "TinyMVC",
        "NOVA Framework"
    ],
    "Specialized Frameworks": [
        "Medoo (Database)",
        "SabreDAV (WebDAV/CalDAV)",
        "Swoole (Asynchronous)",
        "Workerman (Socket/Event-Driven)",
        "Opauth (Authentication)",
        "Behat (BDD Testing)",
        "AMPPHP (Concurrency)",
        "ReactPHP (Asynchronous)"
    ]
}

# Streamlit app
def main():
    # Title
    st.title("PHP Frameworks Explorer")

    # Dropdown for selecting framework category at the top
    category = st.selectbox(
        "Select a Framework Category",
        options=list(frameworks.keys()),
        index=0
    )

    # Display the list of frameworks based on selected category
    st.subheader(f"Frameworks in {category}")
    for framework in frameworks[category]:
        st.write(f"- {framework}")

if __name__ == "__main__":
    main()
