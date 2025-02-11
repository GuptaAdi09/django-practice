set -o errexit

pip install -r requirements.txt


echo "Changing directory to theme/static_src..."
cd theme/static_src || exit 1  # Ensure it exists, exit if not

echo "Running npm install in theme/static_src..."
npm install  # Install dependencies

echo "Building Tailwind CSS..."
npm run build:tailwind  # Ensure this script is in package.json

echo "Moving back to the root directory..."
cd ../../  # Back to project root

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Applying migrations..."
python manage.py migrate

echo "Build script completed successfully!"

python manage.py collectstatic --no-input
python manage.py migrate
if [[ $CREATE_SUPERUSER ]];
then 
    python manage.py createsuperuser --no-input --email "$DJANGO_SUPERUSER_EMAIL"
fi