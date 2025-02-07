from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='Bruxo_XL', email='bruxo@mail.com', password='minh@senh_a'
    )

    session.add(user)
    session.commit()
    # session.refresh(user)
    result = session.scalar(select(User).where(User.email == 'bruxo@mail.com'))

    # assert user.id == 1
    assert result.username == 'Bruxo_XL'
