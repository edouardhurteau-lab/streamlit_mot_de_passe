import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_authenticator import Authenticate

# --- Authentification ---
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attemps': 0,
            'logged_in': False,
            'role': 'utilisateur'
        },
        'Bob': {
            'name': 'Bob',
            'password': 'éponge',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,
            'logged_in': False,
            'role': 'administrateur'
        }
    }
}

authenticator = Authenticate(
    lesDonneesDesComptes,
    "cookie name",
    "cookie key",
    30,
)

# --- Login box ---
authenticator.login()

# --- Contenu ---
def accueil():
    st.title("Espace réservé aux utilisateurs connectés")


# === SI CONNECTÉ ===
if st.session_state["authentication_status"]:
    
    accueil()
    utilisateur = st.session_state["name"]  # Récupération automatique du nom
    st.title(f"Bienvenue sur mon site, {utilisateur} !")

    # Menu latéral
    add_selectbox = st.sidebar.selectbox(
        f"Welcome {utilisateur}",
        ("Accueil", "Photos")
    )

    authenticator.logout("Déconnexion", location="sidebar")

    # Pages
    if add_selectbox == "Accueil":
        st.write("Tu es sur la page d'accueil !")
        st.image("menthes.jpg")
    
    elif add_selectbox == "Photos":
        st.write("Tu es sur mon album photo")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.image("gazelle.jpg")
            st.header("Etrange...")

        with col2:
            st.image("cheval.jpg")

        with col3:
            st.image("pigeon.jpg")
            st.header("Caché !")


elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est incorrect")

elif st.session_state["authentication_status"] is None:
    st.title("salut 'Bob' l' 'éponge', mets ton prénom et ton nom et découvre mon site 😉")
    st.warning("Les champs username et mot de passe doivent être remplis")